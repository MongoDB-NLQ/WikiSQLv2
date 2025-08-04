import os
import shutil
from src._2_preprocess.preprocess_data import preprocess_dataset
from src._3_results.create_database_and_results import create_database_and_results
from src._4_consistent_case.match_question_with_conds import match_questions_with_conds_and_produce_results

def preprocess_every_dataset(questions_paths, tables_path, empty_columns_paths):
    print('Starting preprocessing of datasets...')
    input_dir = '1_original_data'
    output_dir = '2_preprocessed_data'

    for q, t, e in zip(questions_paths, tables_path, empty_columns_paths):
        print(f'Preprocessing {t} and {q}...')
        preprocess_dataset(
            tables_path=f'{input_dir}/{t}',
            questions_path=f'{input_dir}/{q}',
            out_tables_path=f'{output_dir}/{t}',
            out_questions_path=f'{output_dir}/{q}',
            empty_columns_path=e
        )

    print('Preprocessing completed for all datasets.\n')


def construct_database_and_create_result_file(database_names, tables_paths, questions_paths):
    print('Starting getting results...')
    input_dir = '2_preprocessed_data'
    output_dir = '3_results'

    for d, t, q in zip(database_names, tables_paths, questions_paths):
        create_database_and_results(database_name=d,
                                    tables_path=f'{input_dir}/{t}', 
                                    questions_path=f'{input_dir}/{q}',
                                    output_folder_name=output_dir,
                                    scripts_dir=f'{output_dir}/database_scripts'
        )
        # Copy questions to output folder
        shutil.copy2(
            f'{input_dir}/{q}',
            f'{output_dir}/{q}'
        )
        # Copy tables to output folder
        shutil.copy2(
            f'{input_dir}/{t}',
            f'{output_dir}/{t}'
        )

    print('...Results queried for all databases.\n')


def consistent_case_conds_and_questions(databases_names, questions_paths, results_case_sensitive, results_case_insensitive):
    print('Starting naming conds and question consistent...')
    input_folder = '3_results'
    output_folder = '4_consistent_case'

    for d, q, rs, ri in zip(databases_names, questions_paths, results_case_sensitive, results_case_insensitive):
        match_questions_with_conds_and_produce_results(
            database_name=d,
            questions_path=f'{input_folder}/{q}',
            result_case_sensitive_path=f'{input_folder}/{rs}',
            result_case_insensitive_path=f'{input_folder}/{ri}',
            output_results_path=f'{output_folder}/{d}_results.jsonl',
            output_result_case_insensitive_path=f'{output_folder}/{d}_results_case_insensitive.jsonl',
            output_questions_path=f'{output_folder}/{d}.jsonl'
        )
        # Copy tables to output folder
        shutil.copy2(
            os.path.join(input_folder, f'{d}_tables.jsonl'),
            os.path.join(output_folder, f'{d}_tables.jsonl')
        )
        # Copy scripts to output folder
        shutil.copytree(
            os.path.join(input_folder, 'database_scripts'),
            os.path.join(output_folder, 'database_scripts'),
            dirs_exist_ok=True
        )
    print('...FINISHED naming conds and question consistent...\n')


if __name__ == '__main__':
    dirs_to_create = [
        '1_original_data',
        '2_preprocessed_data',
        '3_results',
        '3_results/database_scripts',
        '4_consistent_case',
        '4_consistent_case/database_scripts',
    ]
    for d in dirs_to_create:
        if not os.path.exists(d):
            os.makedirs(d)

    databases = ['dev', 'test', 'train']
    questions = ['dev.jsonl', 'test.jsonl', 'train.jsonl']
    tables = ['dev_tables.jsonl', 'test_tables.jsonl', 'train_tables.jsonl']
    results_case_sensitive = ['dev_results.jsonl', 'test_results.jsonl', 'train_results.jsonl']
    results_case_insensitive = ['dev_results_case_insensitive.jsonl', 'test_results_case_insensitive.jsonl', 'train_results_case_insensitive.jsonl']
    empty_column_dir = 'empty_column_names'
    empty_columns = [f'{empty_column_dir}/dev_empty_columns.json', f'{empty_column_dir}/test_empty_columns.json', f'{empty_column_dir}/train_empty_columns.json']

    # 1:
    preprocess_every_dataset(questions_paths=questions, tables_path=tables, empty_columns_paths=empty_columns)

    # 2:
    construct_database_and_create_result_file(databases, tables, questions)

    # 3:
    consistent_case_conds_and_questions(databases_names=databases, questions_paths=questions, results_case_sensitive=results_case_sensitive, results_case_insensitive=results_case_insensitive)
    
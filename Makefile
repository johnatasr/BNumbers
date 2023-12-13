.PHONY: add_operation_with_valid_value add_operation_with_missing_value invalid_command invalid_argument test_all

add_operation_with_valid_value:
    @python main.py add --value 5

add_operation_with_missing_value:
    @python your_script.py add

stats_operations:
    @python your_script.py stats --value less --value 4
    @python your_script.py stats --value between --value 3,6
    @python your_script.py stats --value greater --value 4

invalid_command:
    @python your_script.py invalid

invalid_argument:
    @python your_script.py add --value string

test_all: add_operation_with_valid_value add_operation_with_missing_value invalid_command invalid_argument

bnumbers:
    @python main.py add --value string


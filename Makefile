pull_sub_module:
	git submodule update --init --recursive

convert:
	find UI -name "*.ui" | cut -d/ -f2 | cut -d. -f1 | xargs -I {} pyside6-uic "UI/{}.ui" -o "Custom_UIs/{}.py"
	#pyside6-uic UI/Single_4BC.ui                  -o Custom_UIs/Single_4BC.py
	#pyside6-uic UI/Mainwindow.ui                  -o Custom_UIs/Mainwindow.py

convert_fix:
	find Custom_UIs -name "*.py" | xargs -I {} misc/Fix-pyside-conversion-types.sh {}
	# misc/Fix-pyside-conversion-types.sh Custom_UIs/Single_4BC.py
	# misc/Fix-pyside-conversion-types.sh Custom_UIs/Mainwindow.py

convert_black:
	find Custom_UIs -name "*.py" | xargs -I {} black {}
	# black Custom_UIs/Single_4BC.py
	# black Custom_UIs/Mainwindow.py

convert_removal_imports:
	find Custom_UIs -name "*.py" | xargs -I {} autoflake --in-place --remove-all-unused-imports {}
	# autoflake --in-place --remove-all-unused-imports Custom_UIs/Single_4BC.py
	# autoflake --in-place --remove-all-unused-imports Custom_UIs/Mainwindow.py

convert_all:
	make clean_convert
	make convert
	make convert_fix
	make convert_black
	make convert_removal_imports


clean_convert:
	find Custom_UIs ! -name '__init__.py' -type f -exec rm -f {} +
	# rm -v Custom_UIs/!(__init__.py)
	# this will leave __init__ without deleting

run:
	python3 main.py

run_from_nix:
	nixGL python3 main.py

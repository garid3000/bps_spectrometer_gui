pull_stubs:
	git clone https://github.com/garid3000/scipy-stubs     ./typings/scipy-stubs
	git clone https://github.com/garid3000/pandas-stubs    ./typings/pandas-stubs
	git clone https://github.com/garid3000/pyqtgraph-stubs ./typings/pyqtgraph-stubs

pull_sub_module:
	git submodule update --init --recursive

clean_convert:
	find Custom_UIs ! -name '__init__.py' -type f -exec rm -f {} +

convert:
	find UI -name "*.ui" -exec basename {} .ui \; | xargs -I {} pyside6-uic "UI/{}.ui" -o "Custom_UIs/{}.py"
	# find UI -name "*.ui" | cut -d/ -f2 | cut -d. -f1 | xargs -I {} pyside6-uic "UI/{}.ui" -o "Custom_UIs/{}.py"

convert_fix:
	find Custom_UIs -name "*.py" | xargs -I {} misc/Fix-pyside-conversion-types.sh {}

convert_black:
	find Custom_UIs -name "*.py" | xargs -I {} black {}

convert_ruff:
	#find Custom_UIs -name "*.py" | xargs -I {} black {}
	ruff format ./Custom_UIs

convert_removal_imports:
	find Custom_UIs -name "*.py" | xargs -I {} autoflake --in-place --remove-all-unused-imports {}

convert_all:
	make clean_convert
	make convert
	make convert_fix # make convert_black
	make convert_ruff
	make convert_removal_imports
	echo "please manualy add 'import QRCs.main_resource' in Custom_UIs/UI_Mainwindow.py"

run:
	export QT_QPA_PLATFORM="xcb" && python3 main.py #python3 main.py

run_from_nix:
	nixGL python3 main.py

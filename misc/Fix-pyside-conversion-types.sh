#!/bin/sh
# sed -i 's///g' "$1"

# Size Policies
sed -i 's/QSizePolicy\.Expanding/QSizePolicy\.Policy\.Expanding/g' "$1"
sed -i 's/QSizePolicy\.Minimum/QSizePolicy\.Policy\.Minimum/g'     "$1"
sed -i 's/QSizePolicy\.Fixed/QSizePolicy\.Policy\.Fixed/g'         "$1"
sed -i 's/QSizePolicy\.Preferred/QSizePolicy\.Policy\.Preferred/g' "$1"
sed -i 's/QSizePolicy\.Ignored/QSizePolicy\.Policy\.Ignored/g'     "$1"

sed -i 's/QTextEdit\.NoWrap/QTextEdit\.LineWrapMode\.NoWrap/g'     "$1"
sed -i 's/QTextEdit\.WidgetWidth/QTextEdit\.LineWrapMode\.WidgetWidth/g'     "$1"
sed -i 's/QTextEdit\.FixedPixelWidth/QTextEdit\.LineWrapMode\.FixedPixelWidth/g'     "$1"
sed -i 's/QTextEdit\.FixedColumnWidth/QTextEdit\.LineWrapMode\.FixedColumnWidth/g'     "$1"

# Size argument Types in funtions Wokrs on both
#setupUi(self, MainWindow):
#retranslatUi(self, MainWindow):
sed -i 's/Ui(self, MainWindow):/Ui(self, MainWindow: QMainWindow) -> None:/g' "$1"
# sed -i 's/Ui(self, GroupBox):/Ui(self, GroupBox: QWidget) -> None:/g'         "$1"
# sed -i 's/Ui(self, Dialog):/Ui(self, Dialog: QDialog) -> None:/g'             "$1"
# sed -i 's/Ui(self, Form):/Ui(self, Form: QWidget) -> None:/g'                 "$1"

# new
sed -i 's/Ui(self, ImagePrepperWidget):/Ui(self, ImagePrepperWidget: QWidget) -> None:/g'      "$1"
sed -i 's/Ui(self, RPiV4L2CtrlDialog):/Ui(self, RPiV4L2CtrlDialog: QWidget) -> None:/g'      "$1"
sed -i 's/Ui(self, IndexCalcShowerGroupBox):/Ui(self, IndexCalcShowerGroupBox: QGroupBox) -> None:/g'      "$1"
sed -i 's/Ui(self, IndexCalcConfigDialog):/Ui(self, IndexCalcConfigDialog: QDialog) -> None:/g'      "$1"
sed -i 's/Ui(self, WarpMatrixDialog):/Ui(self, WarpMatrixDialog: QDialog) -> None:/g'      "$1"
sed -i 's/Ui(self, SelectRegionsDialog):/Ui(self, SelectRegionsDialog: QDialog) -> None:/g'      "$1"




# ???
#
sed -i 's/QFrame\.HLine/QFrame\.Shape\.HLine/g'    "$1"
sed -i 's/QFrame\.VLine/QFrame\.Shape\.VLine/g'    "$1"
sed -i 's/QFrame\.Sunken/QFrame\.Shadow\.Sunken/g' "$1"



# Ver/Hor Slider Related
sed -i 's/Qt\.Vertical/Qt\.Orientation\.Vertical/g'     "$1"
sed -i 's/Qt\.Horizontal/Qt\.Orientation\.Horizontal/g' "$1"

sed -i 's/QSlider\.NoTicks/QSlider\.TickPosition\.NoTicks/g'               "$1"
sed -i 's/QSlider\.TicksAbove/QSlider\.TickPosition\.TicksAbove/g'         "$1"
sed -i 's/QSlider\.TicksLeft/QSlider\.TickPosition\.TicksLeft/g'           "$1"
sed -i 's/QSlider\.TicksBelow/QSlider\.TickPosition\.TicksBelow/g'         "$1"
sed -i 's/QSlider\.TicksRight/QSlider\.TickPosition\.TicksRight/g'         "$1"
sed -i 's/QSlider\.TicksBothSides/QSlider\.TickPosition\.TicksBothSides/g' "$1"

sed -i 's/Qt\.ArrowCursor/Qt\.CursorShape\.ArrowCursor/g'                  "$1"
sed -i 's/Qt\.UpArrowCursor/Qt\.CursorShape\.UpArrowCursor/g'              "$1"
sed -i 's/Qt\.CrossCursor/Qt\.CursorShape\.CrossCursor/g'                  "$1"
sed -i 's/Qt\.WaitCursor/Qt\.CursorShape\.WaitCursor/g'                    "$1"
sed -i 's/Qt\.IBeamCursor/Qt\.CursorShape\.IBeamCursor/g'                  "$1"
sed -i 's/Qt\.SizeVerCursor/Qt\.CursorShape\.SizeVerCursor/g'              "$1"
sed -i 's/Qt\.SizeHorCursor/Qt\.CursorShape\.SizeHorCursor/g'              "$1"
sed -i 's/Qt\.SizeBDiagCursor/Qt\.CursorShape\.SizeBDiagCursor/g'          "$1"
sed -i 's/Qt\.SizeFDiagCursor/Qt\.CursorShape\.SizeFDiagCursor/g'          "$1"
sed -i 's/Qt\.SizeAllCursor/Qt\.CursorShape\.SizeAllCursor/g'              "$1"
sed -i 's/Qt\.BlankCursor/Qt\.CursorShape\.BlankCursor/g'                  "$1"
sed -i 's/Qt\.SplitVCursor/Qt\.CursorShape\.SplitVCursor/g'                "$1"
sed -i 's/Qt\.SplitHCursor/Qt\.CursorShape\.SplitHCursor/g'                "$1"
sed -i 's/Qt\.PointingHandCursor/Qt\.CursorShape\.PointingHandCursor/g'    "$1"
sed -i 's/Qt\.ForbiddenCursor/Qt\.CursorShape\.ForbiddenCursor/g'          "$1"
sed -i 's/Qt\.WhatsThisCursor/Qt\.CursorShape\.WhatsThisCursor/g'          "$1"
sed -i 's/Qt\.BusyCursor/Qt\.CursorShape\.BusyCursor/g'                    "$1"
sed -i 's/Qt\.OpenHandCursor/Qt\.CursorShape\.OpenHandCursor/g'            "$1"
sed -i 's/Qt\.ClosedHandCursor/Qt\.CursorShape\.ClosedHandCursor/g'        "$1"
sed -i 's/Qt\.DragCopyCursor/Qt\.CursorShape\.DragCopyCursor/g'            "$1"
sed -i 's/Qt\.DragMoveCursor/Qt\.CursorShape\.DragMoveCursor/g'            "$1"
sed -i 's/Qt\.DragLinkCursor/Qt\.CursorShape\.DragLinkCursor/g'            "$1"
sed -i 's/Qt\.LastCursor/Qt\.CursorShape\.LastCursor/g'                    "$1"
sed -i 's/Qt\.BitmapCursor/Qt\.CursorShape\.BitmapCursor/g'                "$1"
sed -i 's/Qt\.CustomCursor/Qt\.CursorShape\.CustomCursor/g'                "$1"


























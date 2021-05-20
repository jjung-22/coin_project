import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidgetItem, QProgressBar  #테이블에 표현될 데이터를 정의하기 위한 모듈을 import 
from PyQt5.QtCore import Qt



class OrderbookWidget(QWidget):
    def __init__(self, parent=None, ticker="KRW-ETH"):
        super().__init__(parent)
        uic.loadUi("test/hogawindow.ui", self)
        self.ticker = ticker

    def sell(self):
        for i in range(self.tableBids.rowCount()):
            # 매도호가
            item_0 = QTableWidgetItem(str(""))  #매도 호가 테이블의 1열에 저장될 문자열 객체를 생성하고 오른쪽 정렬
            item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tableAsks.setItem(i, 0, item_0)

            item_1 = QTableWidgetItem(str(""))  #매도 호가 테이블의 2열에 저장될 문자열 객체를 생성하고 오른쪽 정렬
            item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tableAsks.setItem(i, 1, item_1)

            item_2 = QProgressBar(self.tableAsks)  #3열에 저장될 호가 잔량을 시각화 하기위한 QProgressBar 객체를 생성
            item_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  #QProgressBar에 출력될 텍스트는 가운데 정렬
            item_2.setStyleSheet("""
                QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
                QProgressBar::Chunk {background-color : rgba(255, 0, 0, 50%);border : 1}
            """)  #CSS로 셀의 배경 색상을 흰색, ProgressBar의 게이지를 투명도가 부여된 빨강으로 지정
            self.tableAsks.setCellWidget(i, 2, item_2)  #객체를 테이블의 3열에 저장


    def buy(self):
        # 매수호가
        item_0 = QTableWidgetItem(str(""))  #매수 호가 테이블을 표현하기 위한 객체를 미리 생성
        item_0.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.tableBids.setItem(i, 0, item_0)

        item_1 = QTableWidgetItem(str(""))
        item_1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.tableBids.setItem(i, 1, item_1)

        item_2 = QProgressBar(self.tableBids)
        item_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        item_2.setStyleSheet("""
        QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
        QProgressBar::Chunk {background-color : rgba(0, 255, 0, 40%);border : 1} 
        """)  #46라인에서 색상을 투명도가 부여된 파랑으로 만드는 것 이외의 코드는 매도 호가와 같다
        self.tableBids.setCellWidget(i, 2, item_2)



if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ow = OrderbookWidget()
    ow.show()
    exit(app.exec_())
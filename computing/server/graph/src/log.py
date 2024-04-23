import sqlite3
from loguru import logger

class SQLiteSink:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def __call__(self, message):
        record = message.record

        # 构建插入数据的字典
        data = {
            "timestamp": record["time"].strftime("%Y-%m-%d %H:%M:%S.%f"),
            "level": record["level"].name,
            "message": record["message"],
        }
        if record["exception"]:
            data["exception"] = repr(record["exception"])

        # 执行 SQL 插入语句
        columns = ",".join(data.keys())
        placeholders = ",".join("?" * len(data))
        sql = f"INSERT INTO logs ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, tuple(data.values()))

        self.conn.commit()

    def close(self):
        self.conn.close()

# examples/sqlite_sink.py
# # 使用自定义日志处理器
# db_sink = SQLiteSink("app_log.db")
# logger.add(db_sink, backtrace=True, diagnose=True)

# # 开始记录日志
# logger.info("This is an info message.")
# logger.error("An error occurred.", exc_info=True)
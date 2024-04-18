import asyncio
import os 
from collections import deque
from datetime import timedelta
from aiofiles import open as aio_open

class AsyncBufferedLogWriter:
    def __init__(self, log_file_path, flush_interval=timedelta(seconds=10), max_buffer_size=1000):
        self.log_file_path = log_file_path
        self.flush_interval = flush_interval
        self.max_buffer_size = max_buffer_size
        self.buffer = deque(maxlen=max_buffer_size)
        self.last_flush_time = asyncio.get_event_loop().time()

    async def write(self, message):
        self.buffer.append(message)
        if len(self.buffer) >= self.max_buffer_size or (asyncio.get_event_loop().time() - self.last_flush_time) >= self.flush_interval.total_seconds():
            await self._flush()

    async def _flush(self):
        if not self.buffer:
            return

        try:
            async with aio_open(self.log_file_path, "a", encoding="utf-8") as log_file:
                for message in self.buffer:
                    await log_file.write(f"{message}\n")
        except Exception as e:
            # other errors
            pass
        finally:
            self.buffer.clear()
            self.last_flush_time = asyncio.get_event_loop().time()
#    async_log_writer = AsyncBufferedLogWriter(os.path.join(log_directory, "server.log"))
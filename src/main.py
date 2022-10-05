import asyncio
import logging

import grpc
import proto.docs_pb2_grpc as docs_grpc
from docs_service import DocsService

async def serve() -> None:
    server = grpc.aio.server()
    docs_grpc.add_DocsServiceServicer_to_server(DocsService(), server)
    listen_addr = '0.0.0.0:80'
    server.add_insecure_port(listen_addr)

    await server.start()
    logging.info(f"Server started at addr: {listen_addr}")
    await server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
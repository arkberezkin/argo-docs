import logging
import grpc

import proto.docs_pb2 as docs_pb
from proto.docs_pb2_grpc import DocsServiceServicer

class DocsService(DocsServiceServicer):
    async def Documents(
        self, req: docs_pb.DocsRequest, context: grpc.aio.ServicerContext
    ):
        logging.info(f"Documents function was called {req.user_id}")

        if req.user_id == 'error':
            raise ValueError("Error user is calling!")

        return docs_pb.DocsResponse(
            documents=[
                docs_pb.Doc(
                    user_id=req.user_id,
                    title="Hello",
                    text="world",
                ),
            ],
        )
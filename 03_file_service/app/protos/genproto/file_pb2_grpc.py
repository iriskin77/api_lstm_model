# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined use_cases."""
import grpc

import file_pb2 as file__pb2


class FileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFile = channel.stream_unary(
                '/file.File/CreateFile',
                request_serializer=file__pb2.CreateFileRequest.SerializeToString,
                response_deserializer=file__pb2.CreateFileResponse.FromString,
                )
        self.GetFile = channel.unary_unary(
                '/file.File/GetFile',
                request_serializer=file__pb2.GetFileRequest.SerializeToString,
                response_deserializer=file__pb2.GetFileResponse.FromString,
                )


class FileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """rpc GetFiles (GetListFilesRequest) returns (GetListFilesResponse);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFile': grpc.stream_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=file__pb2.CreateFileRequest.FromString,
                    response_serializer=file__pb2.CreateFileResponse.SerializeToString,
            ),
            'GetFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFile,
                    request_deserializer=file__pb2.GetFileRequest.FromString,
                    response_serializer=file__pb2.GetFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'file.File', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class File(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/file.File/CreateFile',
            file__pb2.CreateFileRequest.SerializeToString,
            file__pb2.CreateFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/file.File/GetFile',
            file__pb2.GetFileRequest.SerializeToString,
            file__pb2.GetFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

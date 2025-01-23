from muselsl import stream, list_muses,record

def print_data(data):
    print(data)

muses = list_muses()
print(muses)

record(1000)
# Subscribe to the stream and print incoming data
                       
                                                        


# Note: Streaming is synchronous, so code here will not execute until after the stream has been closed
print('Stream has ended')   
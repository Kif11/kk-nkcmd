import sys

in_seq_path = sys.argv[1]
out_mov_path = sys.argv[2]
start_frame = int(nuke.rawArgs[5])
end_frame = int(nuke.rawArgs[6])

r = nuke.nodes.Read(file=in_seq_path)
r['first'].setValue(start_frame)
r['last'].setValue(end_frame)
w = nuke.nodes.Write(file=out_mov_path, file_type='mov')
w.setInput(0, r)

print 'start_frame: ', start_frame, 'end_frame: ', end_frame

nuke.execute('Write1', start_frame, end_frame)

'''
Created on Feb 12, 2019

@author: mrane
'''
class StackTrace(object):
    def __init__(self, with_call=True, with_return=False,
                       with_exception=False, max_depth=-1):
        self._frame_dict = {}
        self._options = set()
        self._max_depth = max_depth
        if with_call: self._options.add('call')
        if with_return: self._options.add('return')
        if with_exception: self._options.add('exception')

    def __call__(self, frame, event, arg):
        ret = []
        if event == 'call':
            back_frame = frame.f_back
            if back_frame in self._frame_dict:
                self._frame_dict[frame] = self._frame_dict[back_frame] + 1
            else:
                self._frame_dict[frame] = 0

        depth = self._frame_dict[frame]

        if event in self._options\
          and (self._max_depth<0\
               or depth <= self._max_depth):
            ret.append(frame.f_code.co_name)
            ret.append('[%s]'%event)
            if event == 'return':
                ret.append(arg)
            elif event == 'exception':
                ret.append(repr(arg[0]))
            ret.append('in %s line:%s'%(frame.f_code.co_filename, frame.f_lineno))
        if ret:
            print("%s%s"%('  '*depth, '\t'.join([str(i) for i in ret])))

        return self
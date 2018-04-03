# SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            # 1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`
# def approximate_size(size, a_kilobyte_is_1024_bytes=True):

#     '''Convert a file size to human-readable form.
#     Keyword arguments:
#     size -- file size in bytes
#     a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
#                                 if False, use multiples of 1000
#     Returns: string
#     '''
#     if size < 0:
#         raise ValueError('number must be non-negative')

#     multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
#     for suffix in SUFFIXES[multiple]:
#         size /= multiple
#         if size < multiple:
#             return '{0:.1f} {1}'.format(size, suffix)

#     raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(16384, False))
#     print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
#     print(approximate_size(-16384))

# junk = list()
# junk = ['carrots', 'celery', 'kale', 2, ['peas', 'corn']] 
# junk.insert(1, 'kidney beans')
# junk.extend([True, 'tornado'])
# junk.append('hurricane')
# print(junk)

# junk = dict()
# junk = { 'name': 'Steve', 'age': 47, 'role': 'Head Coach' } 
# junk['kids'] = 2
# print(junk)

# junk = set()
# junk.add('Scott')
# print(junk)
# junk.add('Jared')
# print(junk)

# junk = tuple()
# junk = ('Joe', 'Instructor', 'Awesome')
# print(junk)

def display_name(name):
    '''Displays a name
       Takes an argument of the name to be printed.
    ''' 
    print(name)

# display_name('Jared')
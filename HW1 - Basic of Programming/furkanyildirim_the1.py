net_quota = float(input('Please enter your internet quota (GB): '))
video_viewing_time = float(input('Please enter your total video viewing time in minutes: '))
number_of_messages = int(input('Please enter the number of messages you send: '))

video_size = video_viewing_time * 7.7 * 1024 # for KB
message_size = number_of_messages * 1.7 # for KB
net_quota = net_quota * 1024 * 1024

remaining_net_quota = net_quota - video_size - message_size # for KB
video_right_second = remaining_net_quota / (1024 * 7.7 / 60) # for second

video_right_hour = video_right_second // 3600
video_right_minute = (video_right_second - video_right_hour * 3600) // 60
video_right_second = video_right_second - video_right_minute * 60 - video_right_hour * 3600 


print('Your remaining internet quota is {:.2f} GB(s).'.format(remaining_net_quota/ (1024 * 1024)))
print('You can watch video for {} hour(s), {} minute(s) and {:.2f} second(s).'.format(int(video_right_hour),int(video_right_minute),video_right_second))


import json
import datetime

with open('new_json.json', 'r') as file:
    data = json.load(file)

    count_display_id = 0
    count_media_id = 0

    display_id_arr = []
    media_id_arr = []

    for group in data:
        if group['display_id'] not in display_id_arr:
            count_display_id += 1
            display_id_arr.append(group['display_id'])
        if group['media_id'] not in media_id_arr:
            count_media_id += 1
            media_id_arr.append(group['media_id'])

        date_time_str_start = group['t_start']
        date_time_str_end = group['t_end']

        date_time_obj_start = datetime.datetime.strptime(date_time_str_start, '%Y-%m-%d %H:%M:%S.%f')
        date_time_obj_end = datetime.datetime.strptime(date_time_str_end, '%Y-%m-%d %H:%M:%S.%f')
        print('Дата старта:', date_time_obj_start.date())
        print('Время старта:', date_time_obj_start.time())
        print('Дата и время старта:', date_time_obj_start)
        print('Время трансляции:', date_time_obj_end - date_time_obj_start)

    print('Количество display_id =', count_display_id, display_id_arr)
    print('Количество media_id =', count_media_id, media_id_arr)
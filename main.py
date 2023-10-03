import json

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

    print('Количество display_id =', count_display_id, display_id_arr)
    print('Количество media_id =', count_media_id, media_id_arr)
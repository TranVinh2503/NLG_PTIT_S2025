from bs4 import BeautifulSoup
import json

def remove_html(old_data_file,new_data_file):
        # Đọc dữ liệu từ tệp JSON
    with open(old_data_file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for item in data:
        if 'post_content' in item:
            html_content = item['post_content']
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            h2_tags = soup.find_all('h2')
            p_tags = soup.find_all('p')
            
            content_list = []
            
            for h2 in h2_tags:
                content_list.append(h2.text.strip())
            
            for p in p_tags:
                content_list.append(p.text.strip())
            # Ghép nội dung vào một chuỗi duy nhất, mỗi mục cách nhau bằng dấu xuống dòng
            clean_content = '\n'.join(content_list)
            item['post_content'] = clean_content

    # Ghi dữ liệu đã được xử lý vào một tệp JSON mới
    with open(new_data_file, 'w', encoding='utf-8') as new_json_file:
        json.dump(data, new_json_file, ensure_ascii=False, indent=4)

    print("Dữ liệu đã được xử lý và ghi vào file mới.")

def remove_dup_data(old_data_file,new_data_file):
    with open(old_data_file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    seen_data = set()
    unique_data = []
    for item in data:
        # Kiểm tra xem phần tử có phải là một từ điển không
        if isinstance(item, dict):
            post_content = item.get('post_content')
            post_title = item.get('post_title')
            # Kiểm tra xem có cả hai trường post_content và post_title không
            if post_content is not None and post_title is not None:
                # Kiểm tra xem cặp giá trị (post_content, post_title) đã xuất hiện chưa
                if (post_content, post_title) not in seen_data:
                    # Nếu chưa xuất hiện, thêm vào danh sách các mục không trùng lặp
                    unique_data.append(item)
                    # Đánh dấu cặp giá trị (post_content, post_title) là đã xuất hiện
                    seen_data.add((post_content, post_title))
        else:
            print("Phần tử không phải là một từ điển:", item)

    with open(new_data_file, 'w', encoding='utf-8') as new_json_file:
        json.dump(unique_data, new_json_file, ensure_ascii=False, indent=4)

    print("Dữ liệu đã được xử lý và ghi vào file mới.")


# old_data_file: wp_enspire_vn[2024-03-06]/db_post.json
# new_data_file: wp_enspire_vn[2024-03-06]/db_post_formated.json
def main():
    # remove_dup_data('wp_enspire_vn[2024-03-06]/db_post_formated.json','wp_enspire_vn[2024-03-06]/db_post_formated.json')
    remove_html('wp_enspire_vn[2024-03-06]/db_post.json','wp_enspire_vn[2024-03-06]/db_post_formated.json')

if __name__ == '__main__':
    main()
    
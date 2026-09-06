# 📋 Google Form Member Update - Fields Guide

## 🔴 Trường BẮT BUỘC (Required)

| # | Trường | Kiểu | Ví dụ | Ghi chú |
|---|--------|------|-------|---------|
| 1 | **Full Name** | Text | 王宥愷 YU-KAI WANG | Tên đầy đủ (có thể tiếng Anh + Trung) |
| 2 | **Role** | Dropdown | current-master | Chọn từ danh sách roles |
| 3 | **Enter Year** | Number | 2025 | Năm vào lab (YYYY format) |
| 4 | **Image File** | File Upload | Yu-Kai-Wang.jpg | Ảnh đại diện (upload file) |

---

## 🟡 Trường TÙY CHỌN (Optional)

| # | Trường | Kiểu | Ví dụ | Ghi chú |
|---|--------|------|-------|---------|
| 5 | **Aliases** | Text | yu kai wang, yu-kai | Tên gọi khác (cách nhau bằng dấu phẩy) |
| 6 | **Homepage/Portfolio** | URL | https://jason0411202.github.io/ | Trang cá nhân |
| 7 | **Email** | Email | Jason0411202@gmail.com | Email cá nhân |
| 8 | **LinkedIn** | URL | https://linkedin.com/in/username | Profile LinkedIn |
| 9 | **GitHub** | URL | https://github.com/username | GitHub profile |
| 10 | **ORCID** | Text | 0009-0006-7327-9016 | ORCID ID |
| 11 | **Google Scholar** | Text | 1I86inAAAAAJ | Google Scholar ID |
| 12 | **YouTube** | URL | https://youtube.com/watch?v=... | YouTube channel/video |
| 13 | **Facebook** | URL | https://facebook.com/username | Facebook profile |
| 14 | **Instagram** | URL | https://instagram.com/username | Instagram profile |

---

## 📊 Các giá trị cho dropdown Role

```yaml
prof
co-ad
postdoc
current-phd
current-phd-alumni-master
current-master
current-undergrad
current-intern
alumni-master
alumni-phd
alumni-undergraduate
formerMem
```

---

## 🎯 Cấu trúc Google Form đề xuất

### Phần 1: Thông tin cơ bản (Required)
- **Full Name** * (Text field)
- **Role** * (Dropdown - chọn từ danh sách)
- **Enter Year** * (Number field - YYYY)
- **Image File** * (File upload - JPG/PNG)

### Phần 2: Thông tin liên hệ (Optional)
- **Aliases** (Text - dấu phẩy ngăn cách)
- **Email** (Email field)
- **Homepage/Portfolio URL** (URL field)

### Phần 3: Social & Professional (Optional)
- **GitHub URL** (URL field)
- **LinkedIn URL** (URL field)
- **ORCID** (Text field)
- **Google Scholar ID** (Text field)
- **YouTube Channel/Video** (URL field)
- **Facebook Profile** (URL field)
- **Instagram Profile** (URL field)

### Phần 4: Ghi chú (Optional)
- **Additional Notes / Thông tin khác** (Paragraph text)

---

## 💡 Tips & Best Practices

### Dropdown - Sắp xếp theo nhóm:
```
📌 Current Members
  - prof
  - co-ad
  - postdoc
  - current-phd
  - current-phd-alumni-master
  - current-master
  - current-undergrad
  - current-intern

👥 Alumni
  - alumni-master
  - alumni-phd
  - alumni-undergraduate
  - formerMem
```

### File Upload Guidelines:
- ✅ Hạn chế file size: < 5MB
- ✅ Format hỗ trợ: JPG, PNG
- ✅ Khích khích: "Ảnh 400x400px hoặc hình vuông sẽ tốt nhất"

### Validation Rules:
- **Email**: validate format email (abc@domain.com)
- **URLs**: validate URL format (https://...)
- **Enter Year**: chỉ cho phép 4 chữ số (2025, 2026, etc.)
- **Full Name**: yêu cầu không để trống

---

## 📝 Dữ liệu mẫu từ existing members

### Ví dụ 1: Minimal
```yaml
name: Egor
image: images/members/acm003.jpg
role: alumni-master
enteryear: 2020
aliases:
  - egor
```

### Ví dụ 2: Đầy đủ
```yaml
name: 杜有富 Do Huu Phu
image: images/members/311540015.jpg
role: current-phd
enteryear: 2023
aliases:
  - huu phu do
links:
  home-page: https://personal-page-github-io.vercel.app/
  orcid: 0009-0006-7327-9016
  google-scholar: 1I86inAAAAAJ
  youtube: watch?v=ABCDEF0FLWw
  linkedin: do-huu-phu-6734771a7
```

### Ví dụ 3: Với social media
```yaml
name: 狄豪飛 Jorge Tyrakowski
image: images/members/Jorge_Tyrakowski.jpg
role: current-undergrad
enteryear: 2025
aliases:
  - Jorge Tyrakowski
links:
  github: jorgetyrakowski
```

---

## 🔗 Mapping: Google Form → Member Markdown File

| Google Form Field | Markdown Field | Format |
|-------------------|----------------|--------|
| Full Name | `name` | String |
| Role | `role` | Predefined value |
| Enter Year | `enteryear` | Number (YYYY) |
| Image File | `image` | `images/members/{filename}` |
| Aliases | `aliases` | List (lowercase) |
| Homepage/Portfolio | `links.home-page` | URL |
| Email | `links.email` (commented) | String |
| LinkedIn | `links.linkedin` | String hoặc URL |
| GitHub | `links.github` | String hoặc URL |
| ORCID | `links.orcid` | String |
| Google Scholar | `links.google-scholar` | String |
| YouTube | `links.youtube` | String hoặc URL |
| Facebook | `links.facebook` | String hoặc URL |
| Instagram | `links.instagram` | String hoặc URL |

---

## 🔧 Xử lý dữ liệu sau khi submit Google Form

### Python Script Example:
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yaml
import os

# Lấy dữ liệu từ Google Sheet (Google Form responses)
# Tạo markdown file .md tương ứng
# Đặt trong folder _members/

def create_member_file(row_data):
    """
    row_data: dict containing form responses
    """
    name = row_data['Full Name']
    
    # Format filename từ name
    filename = name.replace(' ', '-').replace(',', '') + '.md'
    
    # Build markdown frontmatter
    frontmatter = {
        'name': name,
        'image': f"images/members/{row_data['Image File']}",
        'role': row_data['Role'],
        'enteryear': int(row_data['Enter Year']),
    }
    
    # Add optional aliases
    if row_data.get('Aliases'):
        aliases = [a.strip().lower() for a in row_data['Aliases'].split(',')]
        frontmatter['aliases'] = aliases
    
    # Add links
    links = {}
    if row_data.get('Homepage/Portfolio'):
        links['home-page'] = row_data['Homepage/Portfolio']
    if row_data.get('GitHub'):
        links['github'] = row_data['GitHub'].replace('https://github.com/', '')
    if row_data.get('LinkedIn'):
        links['linkedin'] = row_data['LinkedIn']
    # ... add more links
    
    if links:
        frontmatter['links'] = links
    
    # Write to file
    filepath = f"_members/{filename}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(yaml.dump(frontmatter, allow_unicode=True))
        f.write('---\n')
    
    return filepath

```

---

## 🚀 Workflow Summary

1. **Tạo Google Form** → với các fields theo cấu trúc trên
2. **Share form** → với team members
3. **Collect responses** → đợi submissions
4. **Chạy script** → convert responses → markdown files
5. **Review** → kiểm tra dữ liệu
6. **Git commit & push** → deploy website

---

## 📌 Notes

- Luôn yêu cầu người dùng confirm role chính xác
- Image file phải có tên match với member name (hoặc ghi chú rõ ràng)
- Aliases giúp tìm kiếm, nên lowercase và unique
- Links là optional, nhưng nên khuyến khích điền để profile đầy đủ hơn



- Tạo file babel.cfg

    /babel.cfg

    [python: **.py]

- Chạy lệnh pybabel đi kèm với Babel để trích xuất các chuỗi

    pybabel extract -F babel.cfg -o messages.pot .

- Nếu sử dụng lazy_gettext() 

    pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .

- Tạo bản dịch đầu tiên

    pybabel init -i messages.pot -d translations -l <ngôn ngữ>

- Biên dịch các bản dịch để sử dụng

    pybabel compile -d translations

    
    pybabel update -i messages.pot -d translations
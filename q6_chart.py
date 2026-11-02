import duckdb  # برای اجرای SQL روی فایل parquet
import matplotlib  # کتابخونه‌ی نمودار
matplotlib.use("Agg")  # نمودار رو توی فایل بکش، پنجره‌ی جدا باز نکن
import matplotlib.pyplot as plt  # ابزارهای کشیدن نمودار

# با SQL تعداد سفرهای هر روز رو حساب می‌کنه و به جدول pandas تبدیل می‌کنه
df = duckdb.sql("""
    SELECT CAST(tpep_pickup_datetime AS DATE) AS day, COUNT(*) AS trips
    FROM 'data/clean.parquet'
    GROUP BY day
    ORDER BY day
""").df()

# یه بوم (fig) و یه محور (ax) می‌سازه، اندازه‌ی ۱۱ در ۵ اینچ
fig, ax = plt.subplots(figsize=(11, 5))

# خط نمودار: محور افقی روز، محور عمودی تعداد سفر (تقسیم بر هزار)
# marker="o" یعنی روی هر روز یه نقطه بذار
ax.plot(df["day"], df["trips"] / 1000, marker="o")

ax.set_title("NYC yellow taxi trips per day, January 2015")  # عنوان
ax.set_ylabel("Trips (thousands)")  # اسم محور عمودی
ax.set_xlabel("Day")  # اسم محور افقی
ax.grid(alpha=0.3)  # شبکه‌ی کم‌رنگ پشت نمودار

# فلش توضیحی روی افت طوفان
ax.annotate(
    "Jan 26-27: sharp drop\n(likely the blizzard)",  # متن
    xy=(df["day"][26], df["trips"][26] / 1000),  # نوک فلش: روز ۲۷ ام ژانویه
    xytext=(df["day"][14], 170),  # جای متن روی نمودار
    arrowprops=dict(arrowstyle="->"),  # شکل فلش
)

fig.autofmt_xdate()  # تاریخ‌های محور افقی رو کج می‌کنه تا روی هم نیفتن
fig.tight_layout()  # فاصله‌ها رو تنظیم می‌کنه که چیزی بریده نشه
fig.savefig("daily_trips.png", dpi=150)  # نمودار رو توی فایل png ذخیره می‌کنه
print("saved daily_trips.png")  # پیام تأیید
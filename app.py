import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="پیش‌بینی بیماری قلبی",
    page_icon="❤️",
)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the dataset to understand the format
df = pd.read_csv('Final_Case.csv')

# Mapping of education levels in Persian
education_map = {
    1: 'بی‌سواد',
    2: 'ابتدایی',
    3: 'دیپلم',
    4: 'کارشناسی',
    5: 'کارشناسی ارشد',
    6: 'دکتری'
}

# Define input fields for each variable in Persian
st.title("پیش‌بینی سن بروز بیماری قلبی و عروقی")

st.write("لطفاً جزئیات خود را وارد کنید:")

education = st.selectbox("سطح تحصیلات", list(education_map.values()))
obesity = st.selectbox("چاقی", ["خیر", "بله"])
smoking = st.selectbox("سیگار کشیدن", ["خیر", "بله"])
alcohol = st.selectbox("مصرف الکل", ["خیر", "بله"])
low_pa = st.selectbox("فعالیت بدنی کم", ["خیر", "بله"])
stress = st.selectbox("استرس", ["خیر", "بله"])

diet_skipping_meals = st.selectbox("رژیم: حذف وعده های غذایی", ["خیر", "بله"])
diet_eating_too_quickly = st.selectbox("رژیم: سریع غذا خوردن", ["خیر", "بله"])
diet_high_salt_intake = st.selectbox("رژیم: مصرف زیاد نمک", ["خیر", "بله"])
diet_high_sugar_intake = st.selectbox("رژیم: مصرف زیاد قند", ["خیر", "بله"])
diet_low_fruit_and_vegetable = st.selectbox("رژیم: مصرف کم میوه و سبزیجات", ["خیر", "بله"])
diet_excessive_red_meat = st.selectbox("رژیم: مصرف زیاد گوشت قرمز", ["خیر", "بله"])
diet_skipping_breakfast = st.selectbox("رژیم: حذف صبحانه", ["خیر", "بله"])
diet_inadequate_hydration = st.selectbox("رژیم: کمبود آب بدن", ["خیر", "بله"])
diet_late_night_eating = st.selectbox("رژیم: غذا خوردن در آخر شب", ["خیر", "بله"])

pmh_dm = st.selectbox("سوابق پزشکی: دیابت", ["خیر", "بله"])
pmh_htn = st.selectbox("سوابق پزشکی: فشار خون بالا", ["خیر", "بله"])
pmh_dlp = st.selectbox("سوابق پزشکی: چربی خون بالا", ["خیر", "بله"])
pmh_ckd = st.selectbox("سوابق پزشکی: بیماری کلیوی مزمن", ["خیر", "بله"])
pmh_autoimmune = st.selectbox("سوابق پزشکی: بیماری خودایمنی", ["خیر", "بله"])
pmh_thyroid = st.selectbox("سوابق پزشکی: بیماری تیروئید", ["خیر", "بله"])

type_a = st.selectbox("شخصیت نوع A", ["خیر", "بله"])

# Map the selected education label back to the original number for the model input
education_num = list(education_map.keys())[list(education_map.values()).index(education)]

# Map "بله" to 1 and "خیر" to 0
binary_map = {"خیر": 0, "بله": 1}

age = st.number_input("سن خود را وارد کنید", min_value=0, max_value=120, value=30)

input_data = np.array([[education_num, 
                        binary_map[obesity], binary_map[smoking], binary_map[alcohol], 
                        binary_map[low_pa], binary_map[stress], binary_map[diet_skipping_meals],
                        binary_map[diet_eating_too_quickly], binary_map[diet_high_salt_intake], 
                        binary_map[diet_high_sugar_intake], binary_map[diet_low_fruit_and_vegetable],
                        binary_map[diet_excessive_red_meat], binary_map[diet_skipping_breakfast],
                        binary_map[diet_inadequate_hydration], binary_map[diet_late_night_eating],
                        binary_map[pmh_dm], binary_map[pmh_htn], binary_map[pmh_dlp],
                        binary_map[pmh_ckd], binary_map[pmh_autoimmune], binary_map[pmh_thyroid],
                        binary_map[type_a]]])
#First Hashtag: Predict button
# if st.button("پیش‌بینی سن بروز بیماری قلبی و عروقی"):
    # Perform the prediction
    #prediction = model.predict(input_data)
    
    # Display the prediction
    #st.write(f"سن بروز بیماری قلبی و عروقی پیش‌بینی‌شده: **{float(prediction[0]):.2f}** سال")

    # Lifestyle and Nutrition Consultation Section

# Second hashtagdef assess_risk(predicted_age):
    # if predicted_age > 64:
        # return "پایین"
    # elif 50 <= predicted_age <= 62:
        # return "متوسط"
    # else:
        #return "بالا"

# if st.button("پیش‌بینی سن بروز بیماری قلبی و عروقی"):
    # Perform the prediction
    # prediction = model.predict(input_data)
    # predicted_age = float(prediction[0])

    # Assess the risk
    #risk_level = assess_risk(predicted_age)

    # Display the prediction and risk level
    # st.write(f"سطح خطر بیماری قلبی و عروقی شما: **{risk_level}** است.")


def assess_risk(predicted_age):
    if predicted_age < 50:
        return "کمتر از 50 سال"
    elif 50 <= predicted_age <= 60:
        return "بین 50 تا 60 سال"
    elif 60 < predicted_age <= 70:
        return "بین 60 تا 70 سال"
    else:
        return "بالای 70 سال است"

if st.button("پیش‌بینی سن بروز بیماری قلبی و عروقی"):
    # Perform the prediction
    prediction = model.predict(input_data)
    predicted_age = float(prediction[0])

    # Assess the risk
    risk_level = assess_risk (predicted_age)
    
    st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'Sahel';
        src: url('Fonts/Sahel-SemiBold.woff') format('woff');
    }}
    .custom-text {{
        font-family: 'Sahel', sans-serif;
        font-size: 22px;
        font-weight: bold;
        direction: rtl;
        text-align: right;
    }}
    </style>
    <div class="custom-text">
        براساس اطلاعات فعلی شما، مدل ما پیش‌بینی می‌کند که شما احتمالا اولین حادثه ی قلبی عروقی خود را در بازه ی سنی {risk_level} سال تجربه می کنید.
        این به این معنا نیست که این اتفاق حتماً می‌افتد، اما این عدد نشان دهنده ی این است که اگر وضعیت سلامتی شما به همین شکل باقی بماند، تا چه میزان در معرض این خطر هستید.
        خبر خوب این است که با ایجاد تغییراتی مانند بهبود رژیم غذایی، ترک سیگار و افزایش فعالیت بدنی، می‌توانید این خطر را کاهش داده و سلامت قلب خود را بهبود بخشید.
    </div>
    """, unsafe_allow_html=True)


    #st.write(f"براساس اطلاعات فعلی شما، مدل ما پیش‌بینی می‌کند که شما ممکن است اولین مشکل قلبی خود را در بازه ی سنی **{risk_level}** سال تجربه کنید.")
    #st.write(f"این به این معنا نیست که این اتفاق حتماً می‌افتد، اما این عدد نشان دهنده ای این است که اگر وضعیت سلامتی شما به همین شکل باقی بماند، تا چه میزان در معرض این خطرات هستید.")
    # st.write("خبر خوب این است که با ایجاد تغییراتی مانند بهبود رژیم غذایی، ترک سیگار و افزایش فعالیت بدنی، می‌توانید این خطر را کاهش داده و سلامت قلب و عروق خود را بهبود بخشید.")

    recommendations = []
    
    # Obesity
    if obesity == "بله":
        recommendations.append("چاقی یکی از عوامل مهم در بروز بیماری‌های قلبی و عروقی است. برای کاهش وزن، رژیم غذایی متعادل و فعالیت بدنی منظم را رعایت کنید. هدف شما باید کاهش حداقل ۵ تا ۱۰ درصد از وزن بدن باشد تا تاثیر مثبت بر سلامت قلب داشته باشد.")

    # Smoking
    if smoking == "بله":
        recommendations.append("سیگار کشیدن یکی از مهمترین عوامل خطرزا برای بیماری‌های قلبی و عروقی است. ترک سیگار می‌تواند خطر بروز این بیماری‌ها را به طور چشمگیری کاهش دهد. استفاده از کمک‌های تخصصی مانند مشاوره ترک سیگار یا داروها می‌تواند به شما در ترک سیگار کمک کند.")

    # Alcohol Consumption
    if alcohol == "بله":
        recommendations.append("مصرف بیش از حد الکل می‌تواند فشار خون را افزایش دهد و به قلب آسیب بزند. توصیه می‌شود که مصرف الکل را به حداقل برسانید و در حد اعتدال مصرف کنید. برای مردان، بیش از دو واحد و برای زنان بیش از یک واحد در روز توصیه نمی‌شود.")

    # Physical Inactivity (Low Physical Activity)
    if low_pa == "بله":
        recommendations.append("فعالیت بدنی منظم یکی از مهمترین عوامل در حفظ سلامت قلب است. توصیه می‌شود حداقل ۱۵۰ دقیقه فعالیت بدنی متوسط یا ۷۵ دقیقه فعالیت بدنی شدید در هفته داشته باشید. پیاده‌روی سریع، دوچرخه‌سواری یا شنا می‌تواند به بهبود سلامت قلب کمک کند.")

    # Stress
    if stress == "بله":
        recommendations.append("استرس مزمن می‌تواند خطر بروز بیماری‌های قلبی را افزایش دهد. یادگیری تکنیک‌های مدیریت استرس مانند مدیتیشن، تنفس عمیق، یا یوگا می‌تواند به کاهش استرس کمک کند. همچنین برنامه‌ریزی برای اوقات فراغت و انجام فعالیت‌های لذت‌بخش می‌تواند تاثیر مثبتی بر سلامت قلب داشته باشد.")

    # Diet: Skipping Meals
    if diet_skipping_meals == "بله":
        recommendations.append("حذف وعده‌های غذایی می‌تواند به افزایش وزن و نوسانات قند خون منجر شود که هر دو عامل خطرزا برای سلامت قلب هستند. بهتر است وعده‌های غذایی را به طور منظم و متعادل مصرف کنید. سعی کنید هر سه وعده اصلی را در طول روز داشته باشید و میان‌وعده‌های سالم مانند میوه‌ها و آجیل مصرف کنید.")

    # Diet: Eating Too Quickly
    if diet_eating_too_quickly == "بله":
        recommendations.append("سریع غذا خوردن می‌تواند باعث افزایش وزن و مشکلات گوارشی شود. توصیه می‌شود که هر لقمه را به خوبی بجوید و زمان بیشتری را برای غذا خوردن اختصاص دهید. این کار می‌تواند به هضم بهتر غذا و کاهش احتمال پرخوری کمک کند.")

    # Diet: High Salt Intake
    if diet_high_salt_intake == "بله":
        recommendations.append("مصرف زیاد نمک می‌تواند باعث افزایش فشار خون و افزایش خطر بروز بیماری‌های قلبی شود. توصیه می‌شود مصرف نمک خود را کاهش دهید و به جای نمک از ادویه‌های طبیعی برای طعم‌دهی به غذا استفاده کنید. هدف شما باید مصرف کمتر از ۵ گرم نمک در روز باشد.")

    # Diet: High Sugar Intake
    if diet_high_sugar_intake == "بله":
        recommendations.append("مصرف زیاد قند می‌تواند به افزایش وزن، دیابت و افزایش خطر بیماری‌های قلبی منجر شود. بهتر است مصرف قندهای افزودنی مانند نوشابه‌های شیرین، شیرینی‌ها و دسرها را محدود کنید. به جای آن، از میوه‌های تازه به عنوان منبع طبیعی قند استفاده کنید.")

    # Diet: Low Fruit and Vegetable Intake
    if diet_low_fruit_and_vegetable == "بله":
        recommendations.append("مصرف کم میوه‌ها و سبزیجات می‌تواند به کمبود ویتامین‌ها و مواد معدنی مهم و افزایش خطر بیماری‌های قلبی منجر شود. سعی کنید روزانه حداقل ۵ وعده میوه و سبزیجات مصرف کنید. انواع مختلف میوه‌ها و سبزیجات را در رژیم غذایی خود بگنجانید تا از مزایای تغذیه‌ای آن‌ها بهره‌مند شوید.")

    # Diet: Excessive Red Meat
    if diet_excessive_red_meat == "بله":
        recommendations.append("مصرف زیاد گوشت قرمز و فرآوری شده می‌تواند خطر بروز بیماری‌های قلبی را افزایش دهد. بهتر است مصرف گوشت قرمز را به ۲ تا ۳ بار در هفته محدود کنید و به جای آن از پروتئین‌های گیاهی مانند لوبیا، عدس و مغزها استفاده کنید.")

    # Diet: Skipping Breakfast
    if diet_skipping_breakfast == "بله":
        recommendations.append("حذف صبحانه می‌تواند به افزایش وزن و کاهش انرژی در طول روز منجر شود. مصرف یک صبحانه سالم شامل غلات کامل، میوه‌ها و پروتئین می‌تواند به حفظ انرژی و کاهش خطر بیماری‌های قلبی کمک کند.")

    # Diet: Inadequate Hydration
    if diet_inadequate_hydration == "بله":
        recommendations.append("کمبود آب بدن می‌تواند به خستگی، کاهش تمرکز و افزایش فشار خون منجر شود. توصیه می‌شود که روزانه حداقل ۸ لیوان آب مصرف کنید. همچنین می‌توانید از مایعات سالم دیگر مانند چای گیاهی و آبمیوه‌های طبیعی نیز استفاده کنید.")

    # Diet: Late Night Eating
    if diet_late_night_eating == "بله":
        recommendations.append("خوردن غذا در آخر شب می‌تواند به افزایش وزن و مشکلات گوارشی منجر شود. بهتر است آخرین وعده غذایی خود را حداقل ۲ تا ۳ ساعت قبل از خواب مصرف کنید و از غذاهای سبک و سالم استفاده کنید.")

    if recommendations:
        st.markdown("""
            <div style='text-align: center; font-size: 18px; margin-top: 30px;'>
                مشاوره تغذیه و سبک زندگی
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div style="direction: rtl; text-align: right; margin-right: 20px;">
            <ul style="list-style-type: none; direction: rtl; text-align: right;">
            """, unsafe_allow_html=True)

        # Display the recommendations as bullet points
        for rec in recommendations:
            st.markdown(f"<li>{rec}</li>", unsafe_allow_html=True)

        st.markdown("</ul></div>", unsafe_allow_html=True)

    else:
        st.write("سبک زندگی و رژیم غذایی شما به نظر مناسب است. با ادامه این روند، می‌توانید از سلامتی خود محافظت کنید.")
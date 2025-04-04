import streamlit as st
import random

SORRY = "😢 Sorry, I only tell jokes. \n معاف کیجئے، میں صرف جوکس سناتا ہوں۔"
JOKES = [
    "😂 Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk!\n\n🤣 صوفیہ کریانے کی دکان پر جا رہی تھی۔ ایک پروگرامر نے کہا: ایک لیٹر دودھ لے آنا، اور اگر ان کے پاس انڈے ہوں تو 12 لے آنا۔ صوفیہ 13 لیٹر دودھ لے آئی!",
    "🤣 Why do programmers prefer dark mode? Because light attracts bugs! 👨‍💻\n\n😆 پروگرامرز ڈارک موڈ کیوں پسند کرتے ہیں؟ کیونکہ روشنی کیڑے مکوڑوں کو اپنی طرف کھینچتی ہے!",
    "😂 How do you comfort a JavaScript bug? You console it! 💻\n\n🤣 جاوا اسکرپٹ کے بگ کو کیسے تسلی دیتے ہیں؟ آپ اسے 'کنسول' کرتے ہیں!",
    "😜 Why was the math book sad? Because it had too many problems. 📖\n\n😂 ریاضی کی کتاب اداس کیوں تھی؟ کیونکہ اس کے پاس بہت زیادہ مسئلے تھے!",
    "😂 Why don't skeletons fight each other? They don't have the guts! ☠️\n\n🤣 ڈھانچے ایک دوسرے سے کیوں نہیں لڑتے؟ کیونکہ ان میں ہمت نہیں ہوتی!",
    "🤣 Teacher: What is the most powerful thing? Student: Prayer, because it is wireless! 🙏\n\n😆 استاد: سب سے طاقتور چیز کیا ہے؟ طالبعلم: دعا، کیونکہ یہ وائرلیس ہوتی ہے!",
    "😂 Doctor: You need rest, why don't you sleep well? Patient: Doctor, I keep dreaming that I'm awake! 😴\n\n🤣 ڈاکٹر: تمہیں آرام کی ضرورت ہے، نیند کیوں پوری نہیں ہو رہی؟ مریض: ڈاکٹر صاحب، میں جاگنے کے خواب دیکھتا رہتا ہوں!",
    "😆 Wife to Husband: Give me a sweet nickname! Husband: My life! 😜\n\n😂 بیوی شوہر سے: سنو، مجھے پیار سے کوئی نام دو! شوہر: میری جان!",
    "🤣 Girl: When will you marry me? Boy: When I become rich! Girl: Then you will always be poor! 💔\n\n😂 لڑکی: تم مجھ سے شادی کب کرو گے؟ لڑکا: جب میں امیر ہو جاؤں گا! لڑکی: پھر تم ہمیشہ غریب ہی رہو گے!",
    "😆 What is the best way to watch a fly-fishing tournament? Live stream! 🎣\n\n😂 مچھلی پکڑنے کے مقابلے کو دیکھنے کا سب سے اچھا طریقہ کیا ہے؟ 'لائیو اسٹریم'!",
    "😂 Why do cows have hooves instead of feet? Because they lactose! 🐄\n\n🤣 گائیں کے پاؤں کیوں نہیں ہوتے؟ کیونکہ وہ 'لیکٹوز' کرتی ہیں!",
    "🤣 Man: Doctor, I have memory loss! Doctor: Since when? Man: Since when what? 🤔\n\n😂 آدمی: ڈاکٹر صاحب، مجھے بھولنے کی بیماری ہے! ڈاکٹر: کب سے؟ آدمی: کب سے کیا؟",
    "😜 Customer: This coffee tastes like dirt! Barista: That’s because it was ground this morning! ☕\n\n🤣 گاہک: یہ کافی مٹی جیسی کیوں لگ رہی ہے؟ بارسٹا: کیونکہ یہ آج صبح ہی 'گراؤنڈ' کی گئی تھی!",
    "😆 Wife: You are always on your phone! Husband: Okay, I will leave my phone! Wife: No, I will leave you! 😂\n\n🤣 بیوی: تم ہمیشہ موبائل میں مصروف رہتے ہو! شوہر: اچھا، میں موبائل چھوڑ دیتا ہوں! بیوی: نہیں، میں تمہیں چھوڑ دیتی ہوں!",
    "🤣 Why don’t programmers like nature? It has too many bugs! 🐞\n\n😂 پروگرامرز کو قدرت کیوں پسند نہیں؟ کیونکہ اس میں بہت زیادہ 'بگس' ہوتے ہیں!"
]

st.title("🤖 Joke Bot - English & Urdu")
if st.button("😂 Click me to get Joke"):
    joke = random.choice(JOKES)  
    st.success(joke)  


st.markdown("""
<div class="footer">
    <p>Secure Joke bot v1.0 | Stay Safe Online | <a href="https://github.com/SitesByKashan">Made By M Kashan Malik Awan</a> </p>
</div>
""", unsafe_allow_html=True)
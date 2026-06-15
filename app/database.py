# SQLAlchemy बाट database connection बनाउन 'create_engine' इम्पोर्ट गरिएको हो।
from sqlalchemy import create_engine

# 'declarative_base' ले database को table (models) बनाउन मद्दत गर्छ।
# 'sessionmaker' ले database सँग कुराकानी गर्ने session (वर्कस्पेस) फ्याक्ट्री बनाउँछ।
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

# यो तपाईंको PostgreSQL database को ठेगाना (credentials) हो।
# यसमा 'username', 'password', host ('localhost'), port ('5432') र database को नाम ('dbname') हुन्छ।

# यसले DATABASE_URL प्रयोग गरेर FastAPI र PostgreSQL बीच एउटा मुख्य कनेक्सन पाइप (engine) तयार गर्छ।
engine = create_engine(settings.DATABASE_URL)


# यसले हरेक रिक्वेस्टको लागि छुट्टाछुट्टै काम गर्ने ठाउँ (session) बनाउने फ्याक्ट्री तयार गर्छ।
# autocommit=False: तपाईंले आफैं 'db.commit()' नभनेसम्म डेटा सेभ हुँदैन।
# autoflush=False: आवश्यकता नभएसम्म अनाबश्यक रूपमा डेटाबेसमा डेटा पठाउँदैन।
# bind=engine: यसले माथि बनाएको मुख्य 'engine' पाइप प्रयोग गर्छ।
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# यसले एउटा Base क्लास बनाउँछ। तपाईंको एपको सबै database tables (जस्तै User, Todo) यही Base क्लास प्रयोग गरेर बन्छन्।
Base = declarative_base()


# यो FastAPI को एउटा 'Dependency' हो, जसले हरेक API रिक्वेस्ट आउँदा database session दिने काम गर्छ।
def get_db():
    # १. फ्याक्ट्रीबाट एउटा नयाँ र छुट्टै database session (db) खोल्छ।
    db = SessionLocal()
    try:
        # २. यो session लाई FastAPI को route (endpoint) मा प्रयोग गर्न पठाउँछ (yield गर्छ)।
        yield db
    finally:
        # ३. API को काम सकिएपछि database को session लाई सुरक्षित रूपमा बन्द (close) गरिदिन्छ।
        db.close()

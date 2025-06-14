###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
# 1. flo_data_20K.csv verisini okuyunuz.
# 2. Veri setinde
# a. İlk 10 gözlem,
# b. Değişken isimleri,
# c. Betimsel istatistik,
# d. Boş değer,
# e. Değişken tipleri, incelemesi yapınız.
# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
# alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
# 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

# GÖREV 2: RFM Metriklerinin Hesaplanması

# GÖREV 3: RF ve RFM Skorlarının Hesaplanması

# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması

# GÖREV 5: Aksiyon zamanı!
# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
# ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
# yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
# alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################

import pandas as pd
import datetime as dt

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.width', 500)

###############################################################
# 1. flo_data_20K.csv verisini okuyunuz. Dataframe'in kopyasını oluşturunuz.

df_ = pd.read_csv('0_Cases_and_Projects/FLO_Customer_Segmentation/flo_data_20k.csv')
df = df_.copy()

###############################################################
# 2. Veri setinde
# a. İlk 10 gözlem,
# b. Değişken isimleri,
# c. Boyut,
# d. Betimsel istatistik,
# e. Boş değer,
# f. Değişken tipleri, incelemesi yapınız.

# a. İlk 10 gözlem

df.head(10)

# b. Değişken isimleri,

df.columns

# c. Boyut,

df.shape

# d. Betimsel istatistik,

df.describe().T

# e. Boş değer,

df.isnull().sum()

# f. Değişken tipleri, incelemesi yapınız.

df.info()

df['master_id'].nunique()

###############################################################
# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.

df['order_num_total'] = df['order_num_total_ever_online'] + df['order_num_total_ever_offline']
df['customer_value_total'] = df['customer_value_total_ever_online'] + df['customer_value_total_ever_offline']

###############################################################
# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
# df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)

date_columns = ['first_order_date', 'last_order_date', 'last_order_date_online', 'last_order_date_offline']
for col in date_columns:
    df[col] = pd.to_datetime(df[col])

df.info()

###############################################################
# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız. 

channel_analysis = df.groupby('order_channel').agg({
    'master_id': 'nunique',
    'order_num_total': 'sum',
    'customer_value_total': 'sum'
}).rename(columns={
    'master_id': 'customer_count',
    'order_num_total': 'total_orders',
    'customer_value_total': 'total_revenue'
}).sort_values(by='customer_count', ascending=False)

###############################################################
# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
# En fazla harcama yapan ilk 10 müşteriyi sıralıyoruz

top_10_customer_value = df.sort_values(by='customer_value_total', ascending=False)[
    ['master_id', 'customer_value_total']].reset_index(drop=True).head(10)

###############################################################
# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

top_10_order_num = df.sort_values(by='order_num_total', ascending=False)[
    ['master_id', 'order_num_total']].reset_index(drop=True).head(10)

###############################################################
# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def prepare_data(dataframe):

    # Tarih değişkenlerini datetime formatına çevir
    date_columns = ['first_order_date', 'last_order_date',
                    'last_order_date_online', 'last_order_date_offline']
    for col in date_columns:
        dataframe[col] = pd.to_datetime(dataframe[col])

    # Toplam sipariş ve toplam harcama değişkenlerini oluştur
    dataframe['order_num_total'] = dataframe['order_num_total_ever_online'] + dataframe['order_num_total_ever_offline']
    dataframe['customer_value_total'] = dataframe['customer_value_total_ever_online'] + dataframe['customer_value_total_ever_offline']

    # Alışveriş kanallarındaki müşteri sayısı, toplam sipariş sayısı ve toplam harcama
    channel_analysis = dataframe.groupby('order_channel').agg({
        'master_id': 'nunique',
        'order_num_total': 'sum',
        'customer_value_total': 'sum'
    }).rename(columns={
        'master_id': 'customer_count',
        'order_num_total': 'total_orders',
        'customer_value_total': 'total_revenue'
    }).sort_values(by='customer_count', ascending=False)

    print(f'Alışveriş kanallarındaki müşteri sayısı, toplam sipariş sayısı ve toplam harcama:\n{channel_analysis}\n')
    print('#################################################################\n')

    # En fazla harcama yapan ilk 10 müşteriyi sırala
    top_10_customer_value = dataframe.sort_values(by='customer_value_total', ascending=False)[
        ['master_id', 'customer_value_total']].reset_index(drop=True).head(10)

    print(f'En fazla harcama yapan ilk 10 müşteri:\n{top_10_customer_value}\n')
    print('#################################################################\n')

    # En fazla siparişi veren ilk 10 müşteriyi sırala
    top_10_order_num = dataframe.sort_values(by='order_num_total', ascending=False)[
        ['master_id', 'order_num_total']].reset_index(drop=True).head(10)

    print(f'En fazla siparişi veren ilk 10 müşteri:\n{top_10_order_num}\n')
    print('#################################################################\n')

    return dataframe

df = df_.copy()
df = prepare_data(df)

###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi

today_date = df['last_order_date'].max() + dt.timedelta(days=2)

# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe

# RFM metriklerini hesapla
rfm = df.groupby('master_id').agg(
    {'last_order_date': lambda last_order_date: (today_date - last_order_date.max()).days,
     'order_num_total': lambda order_num_total: order_num_total,
     'customer_value_total': lambda customer_value_total: customer_value_total.sum()})

# RFM metriklerine uygun isimler ver
rfm.columns = ['recency', 'frequency', 'monetary']
rfm.index.name = 'customer_id'

####################

# alternatif
rfm = pd.DataFrame()
rfm['customer_id'] = df['master_id']
rfm['recency'] = (today_date - df['last_order_date']).dt.days
rfm['frequency'] = df['order_num_total']
rfm['monetary'] = df['customer_value_total']


###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

# Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çeviriniz.
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydediniz.
# recency_score ve frequency_score’u tek bir değişken olarak ifade ediniz ve RF_SCORE olarak kaydediniz.

rfm['recency_score'] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['frequency_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['monetary_score'] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

rfm['RF_SCORE'] = rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str)

###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için
# segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_risk',
    r'[1-2]5': 'cant_lose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)


###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[['segment', 'recency', 'frequency', 'monetary']].groupby('segment').agg(['mean', 'count'])

# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.


# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.

female_customers = df[df['interested_in_categories_12'].str.contains('KADIN')]
a_target = rfm[
    (rfm['segment'].isin(['champions', 'loyal_customers'])) &
    (rfm.index.isin(female_customers['master_id']))
    ].index

a_target.to_frame(name='customer_id').to_csv('female_customers_id.csv', index=False)


# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.


male_child_customers = df[df['interested_in_categories_12'].str.contains('ERKEK|COCUK')]
b_target = rfm[
    (rfm['segment'].isin(['cant_lose', 'about_to_sleep', 'new_customers'])) &
    (rfm.index.isin(male_child_customers['master_id']))
    ].index

b_target.to_frame(name='customer_id').to_csv('man_child_customers_id.csv', index=False)

















































































































































































































































































































































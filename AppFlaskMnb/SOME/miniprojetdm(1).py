# -*- coding: utf-8 -*-
"""MiniProjetDM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bzZdB-RMIqb2GKA1LZB1riAEpavCeXJB
"""

# !pip install scikit-plot
import pandas as pd
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score , confusion_matrix, classification_report

"""#exploration des donnees

"""

from google.colab import files
uploaded = files.upload()

# df = pd.read_csv('spam_ham_dataset.csv', sep='\t', names=['label', 'messages'])
df = pd.read_csv('spam_ham_dataset.csv')

print(df.head())

df = df[['text', 'label_num']]

print(df.head(10))
# print(df['text'].iloc[1000])

count_Class = pd.value_counts(df.label_num, sort = True)

# Data to Plot
labels = 'NotSpam', 'Spam'
sizes = [count_Class[0], count_Class[1]]
colors = ['green', 'red']
explode = (0.1, 0.1)

# Plot
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.axis('equal')
plt.show()

"""#pre-conception de modele"""

X_train, X_test, y_train, y_test = tts(df['text'], df['label_num'], test_size=0.2, random_state=1)

#vectorizing the data
count_vector = CountVectorizer()
train_data = count_vector.fit_transform(X_train)
test_data = count_vector.transform(X_test)

print(f"{train_data}\n avec shape : {train_data.shape}")

"""#Naïve Bayes classifier for multinomial models"""

Mnb = MultinomialNB()
Mnb.fit(train_data, y_train)

"""#Now we predict"""

MnbPredicts = Mnb.predict(test_data)
print(f"on a MnbPredicts est :\n {MnbPredicts} \n avec shape est : {MnbPredicts.shape}")

print("The accuracy of our Naïve Bayes multinomial model is {} %".format(accuracy_score(y_test, MnbPredicts) * 100))
print("The Precision of our Naïve Bayes multinomial model is {} %". format(precision_score(y_test, MnbPredicts)* 100))
print("The Recall of our Naïve Bayes multinomial model is {} %" . format(recall_score(y_test, MnbPredicts)* 100))

"""#We use the confusion matrix to observe the performance of our model."""

confusionmatrix = confusion_matrix(y_test, MnbPredicts)
print(f"The accuracy of Naive Bayes clasifier is {accuracy_score(y_test, MnbPredicts) * 100}")
print("\n", confusionmatrix)
skplt.metrics.plot_confusion_matrix(y_test, MnbPredicts, normalize = True)
plt.show()

"""#Now we want to test our model mbn with a new Sms/Email massage"""

new_test_sample_ham = ["Hi, I'm Mohammad Nabizadeh and I am glad to share the program that I've written with everyone."]
new_test_sample_ham_vectorized = count_vector.transform(new_test_sample_ham)
sample_predict = Mnb.predict(new_test_sample_ham_vectorized)
# Utiliser une expression conditionnelle dans une f-string pour imprimer le résultat
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ["Congratulations, you've won a free Sony camera."]
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ['''Objet : Invitation à une conférence sur la technologie de demain

Cher Youssef,

Nous sommes ravis de vous inviter à notre prochaine conférence sur la technologie de demain qui se tiendra le [Date] à [Lieu]. Cette conférence sera une opportunité unique de découvrir les dernières avancées technologiques et d'explorer les tendances qui façonneront l'avenir.

La conférence comprendra des sessions passionnantes animées par des experts de l'industrie, des démonstrations en direct de nouvelles technologies révolutionnaires et des opportunités de réseautage avec des professionnels du secteur.

Nous croyons que votre expérience et votre expertise apporteront une contribution précieuse à nos discussions, et nous serions honorés de vous avoir parmi nous.

Veuillez trouver ci-joint l'agenda complet de la conférence. N'hésitez pas à nous contacter si vous avez des questions ou des besoins particuliers.

Nous espérons vous voir parmi nous à cette conférence passionnante !

Cordialement,
Votre nom
Adidas
''']
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ["Get rich quick! Buy now, limited offer!"]
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ['''
Subject: Congratulations! You've won $1,000,000!

Dear lucky winner,

We are pleased to inform you that your email address has been selected as the grand prize winner of our annual lottery jackpot! You have won a staggering sum of $1,000,000!

To claim your prize, simply reply to this email with your full name, address, and a copy of your identification. Once we receive your information, we will initiate the transfer of your winnings to your bank account.

Don't miss out on this incredible opportunity to become a millionaire overnight! Reply now to claim your prize.

Best regards,
Lottery Winner Team

''']
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ['''
From: john.doe@example.com
To: jane.smith@example.com
Subject: Invitation to Conference on Artificial Intelligence

Dear Jane,

I hope this email finds you well. I am writing to extend a cordial invitation to you to attend the upcoming Conference on Artificial Intelligence, which will be held in New York City from March 15th to March 17th.

This conference will feature renowned experts in the field of artificial intelligence, with presentations and discussions on topics ranging from machine learning algorithms to ethical considerations in AI development.

As a respected colleague in the field, your insights and contributions would be invaluable to our discussions. We would be honored to have you join us as a speaker on the panel discussing "The Future of AI in Healthcare".

Please let me know at your earliest convenience if you would be interested in participating. I have attached the conference agenda for your reference.

Looking forward to hearing from you soon.

Best regards,
John Doe

''']
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ["Congratulations, you've won a free Sony camera."]
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ["Hello Anas, I hope this email finds you in good health and that you are having a great day. I just wanted to let you know that we are having a team meeting tomorrow at 10:00 in the main conference room. We will discuss recent project progress and next steps. Your presence is important, so please confirm your availability as soon as possible. Please feel free to contact me if you have any questions or concerns. Kind regards, Youssef"]
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ['''
Subject: Invitation to a conference on the technology of tomorrow

Dear Youssef,

We are delighted to invite you to our next conference on tomorrow's technology which will be held on [Date] in [Location]. This conference will be a unique opportunity to discover the latest technological advances and explore the trends that will shape the future.

The conference will feature exciting sessions led by industry experts, live demonstrations of groundbreaking new technologies, and networking opportunities with industry professionals.

We believe that your experience and expertise will make a valuable contribution to our discussions, and we would be honored to have you join us.

Please find attached the full conference agenda. Please do not hesitate to contact us if you have any questions or special needs.

We hope to see you among us at this exciting conference!

Sincerely,
Youssef
Adidas
''']
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

new_test_sample_spam= ['''
Subject: Invitation to Attend Business Networking Event

Dear Youssef,

I hope this email finds you well. I am reaching out to invite you to our upcoming business networking event scheduled for [Date] at [Location].

The event promises to be an excellent opportunity to connect with professionals from various industries, share insights, and explore potential collaborations. We have lined up engaging panel discussions, interactive workshops, and ample networking sessions to facilitate meaningful interactions.

We believe your expertise and experience would greatly enrich the discussions, and we would be honored to have you join us.

Please find attached the detailed agenda for the event. Should you have any questions or require further information, please don't hesitate to reach out.

We look forward to welcoming you to our event and fostering mutually beneficial connections.

Warm regards,
youssef

''']
new_test_sample_spam_vectorized = count_vector.transform(new_test_sample_spam)
sample_predict = Mnb.predict(new_test_sample_spam_vectorized)
print(f"Voici la prédiction du message : {'non-spam' if sample_predict == 0 else 'spam'}")

# !pip install joblib
# !pip install scikit-learn
# !pip install pickle

# from sklearn.externals import joblib

# # Save the trained model
# joblib.dump(Mnb, 'spam_classifier_model.pkl')

# # Save the CountVectorizer
# joblib.dump(count_vector, 'count_vectorizer.pkl')

import pickle

# Save the trained model
with open('spam_classifier_model.pkl', 'wb') as f:
    pickle.dump(Mnb, f)

# Save the CountVectorizer
with open('count_vectorizer.pkl', 'wb') as f:
    pickle.dump(count_vector, f)

# import pickle

# # Load the trained model
# with open('spam_classifier_model.pkl', 'rb') as f:
#     Mnb = pickle.load(f)

# # Load the CountVectorizer
# with open('count_vectorizer.pkl', 'rb') as f:
#     count_vector = pickle.load(f)


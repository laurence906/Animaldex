from floridaPrediction import FloridaSpeciesNet

model = FloridaSpeciesNet(
    'speciesnet-v4.0.2a-weights',
    'florida_fallback.pkl'
)

result = model.predict("training_data/raw_images/5c7ce479-8a45-40b3-ae21-7c97dfae22f5;mammalia;artiodactyla;cervidae;odocoileus;virginianus;white-tailed deer/02240348.JPG")
print(result)

result = model.predict("training_data/raw_images/5c7ce479-8a45-40b3-ae21-7c97dfae22f5;mammalia;artiodactyla;cervidae;odocoileus;virginianus;white-tailed deer/SUNP0169.JPG")
print(result)
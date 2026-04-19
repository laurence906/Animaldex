from floridaPrediction import FloridaSpeciesNet

modelPath = 'kaggle:google/speciesnet/pyTorch/v4.0.2a/1' 

model = FloridaSpeciesNet(
    model_path=modelPath,
    fallback_pkl='florida_fallback.pkl'
)
# for offline usage, download weights from github and hardcode the SpeciesNet model_path as speciesnet-v4.0.2a-weights

print("Enter target file: ")
cin = input()
result = model.predict(cin)
print(result)
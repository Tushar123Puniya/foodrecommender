def calculate_calories(features):
  activity_mappings={
    1:1.2,       # Sedentary (little or no exercise)
    2:1.375,     # Lightly active (light exercise/sports 1-3 days a week)
    3:1.55,      # Moderately active (moderate exercise/sports 3-5 days a week)
    4:1.725,     # Very active (hard exercise/sports 6-7 days a week)
    5:1.9        # Extra active (very hard exercise/sports & physical job or training twice a day
  }
  weight = features['Weight']
  height = features['Height']
  age = features['Age']
  gender = features['Gender']
  activity = features['Activity type']
  height = height/100
  bmi = weight/(height**2)
  bmr = 0

  if gender == 'Male':
    bmr = 88.362 + (13.397 * weight) + (4.799 * height*100) - (5.677 * age)
  else:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height*100) - (4.330 * age)

  w = activity_mappings[activity]

  caloriy_need = w*bmr
  caloriy_need /= 3
  
  if features['Goal']=='Gain':
    caloriy_need += 100
  elif features['Goal']=='Lose':
    caloriy_need -= 100
  return caloriy_need
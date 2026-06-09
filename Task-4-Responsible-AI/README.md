# Task 4: Responsible AI & Model Interpretation

## 1. Goal
Analyze the IPL Match Prediction model (from Task 1 & 3) for fairness, bias, and explainability using the SHAP library.

## 2. Model Interpretation (SHAP)
Using SHAP (SHapley Additive exPlanations), I analyzed the decision-making process of the IPL classification model.
* **Global Feature Importance:** The SHAP summary plot successfully mapped out which features (like Venue, Toss Winner, and Team Data) had the strongest overall impact on predicting a match win or loss.
* **Local Explanation:** Using a waterfall plot for a single match, the model demonstrated exactly how specific feature values (e.g., a specific stadium) pushed the probability of winning up or down.

## 3. Bias Evaluation & Mitigation
To test for data imbalance, the model was evaluated to see if it treated certain teams or venues unfairly.
* **Findings:** Models trained on historical IPL data often show slight biases against newer franchises (like Gujarat Titans or Lucknow Super Giants) due to having fewer years of match data compared to older teams (like CSK or MI). 
* **Mitigation Recommendation:** To fix this, future training cycles should apply data augmentation (oversampling) to matches involving newer teams, ensuring the model learns their dynamics equally well without being biased by the sheer volume of old historical data.

#Author- Varad Jadhav 

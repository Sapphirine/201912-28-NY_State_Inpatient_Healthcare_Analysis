FIELD1_CHOICES= [
    ('Age_Group', 'Age Group'),
    ('Zip_Code___3_digits', 'Zip Code (3 Digits)')]

FIELD2_CHOICES= [
    ('Gender', 'Gender'),
    ('APR_MDC_Description', 'Diagnosis'),
    ('Race', 'Race'),
    ('Ethnicity', 'Ethnicity'),
    ('Type_of_Admission', 'Type of Admission'),
    ('Hospital_Service_Area', 'Hospital Service Area')]

# PREDICTION VARS

ZIP_CODES = [(str(i), str(i)) for i in range(100, 150)]+[('OOS', 'OOS')]

AGE_GROUP = [
    ('0 to 17', '0 to 17'),
    ('18 to 29', '18 to 29'),
    ('30 to 49', '30 to 49'),
    ('50 to 69', '50 to 69'),
    ('70 or Older', '70 or Older')]

RACE_GROUP = [
    ('White', 'White'),
    ('Black/African American', 'Black/African American'),
    ('Other Race', 'Other Race'),
    ('Multi-racial', 'Multi-racial')]

GENDER = [
    # ('U', 'Unknown'),
    ('M', 'Male'),
    ('F', 'Female')]

TYPE_OF_ADMISSION = [
    ('Elective', 'Elective'),
    ('Emergency', 'Emergency'),
    ('Newborn', 'Newborn'),
    ('Not Available', 'Not Available'),
    ('Trauma', 'Trauma'),
    ('Urgent', 'Urgent')]

# HEATMAP VARS



ETHNICITY_GROUP = [
    ('Not Span/Hispanic', 'Not Span/Hispanic'),
    ('Unknown', 'Unknown'),
    ('Spanish/Hispanic', 'Spanish/Hispanic'),
    ('Multi-ethnic', 'Multi-ethnic')
]

CATEGORY_CHOICES = [
    (None, '-----'),
    ('Age_Group', 'Age Group'),
    ('Gender', 'Gender'),
    ('Race', 'Race'),
    ('Ethnicity', 'Ethnicity')
]

DIAGNOSIS_TYPES = [
    ('Abdominal hernia', 'Abdominal hernia'),
    ('Abdominal pain', 'Abdominal pain'),
    ('Acquired foot deformities', 'Acquired foot deformities'),
    ('Acute and chronic tonsillitis', 'Acute and chronic tonsillitis'),
    ('Acute and unspecified renal failure', 'Acute and unspecified renal failure'),
    ('Acute bronchitis', 'Acute bronchitis'),
    ('Acute cerebrovascular disease', 'Acute cerebrovascular disease'),
    ('Acute myocardial infarction', 'Acute myocardial infarction'),
    ('Acute posthemorrhagic anemia', 'Acute posthemorrhagic anemia'),
    ('Adjustment disorders', 'Adjustment disorders'),
    ('Administrative/social admission', 'Administrative/social admission'),
    ('Alcohol-related disorders', 'Alcohol-related disorders'),
    ('Allergic reactions', 'Allergic reactions'),
    ('Anal and rectal conditions', 'Anal and rectal conditions'),
    ('Anxiety disorders', 'Anxiety disorders'),
    ('Aortic and peripheral arterial embolism or thrombosis', 'Aortic and peripheral arterial embolism or thrombosis'),
    ('Aortic; peripheral; and visceral artery aneurysms', 'Aortic; peripheral; and visceral artery aneurysms'),
    ('Appendicitis and other appendiceal conditions', 'Appendicitis and other appendiceal conditions'),
    ('Aspiration pneumonitis; food/vomitus', 'Aspiration pneumonitis; food/vomitus'),
    ('Asthma', 'Asthma'),
    ('Attention-deficit, conduct, and disruptive behavior disorders', 'Attention-deficit, conduct, and disruptive behavior disorders'),
    ('Bacterial infection; unspecified site', 'Bacterial infection; unspecified site'),
    ('Benign neoplasm of uterus', 'Benign neoplasm of uterus'),
    ('Biliary tract disease', 'Biliary tract disease'),
    ('Birth trauma', 'Birth trauma'),
    ('Blindness and vision defects', 'Blindness and vision defects'),
    ('Burns', 'Burns'),
    ('Calculus of urinary tract', 'Calculus of urinary tract'),
    ('Cancer of bladder', 'Cancer of bladder'),
    ('Cancer of bone and connective tissue', 'Cancer of bone and connective tissue'),
    ('Cancer of brain and nervous system', 'Cancer of brain and nervous system'),
    ('Cancer of breast', 'Cancer of breast'),
    ('Cancer of bronchus; lung', 'Cancer of bronchus; lung'),
    ('Cancer of cervix', 'Cancer of cervix'),
    ('Cancer of colon', 'Cancer of colon'),
    ('Cancer of esophagus', 'Cancer of esophagus'),
    ('Cancer of head and neck', 'Cancer of head and neck'),
    ('Cancer of kidney and renal pelvis', 'Cancer of kidney and renal pelvis'),
    ('Cancer of liver and intrahepatic bile duct', 'Cancer of liver and intrahepatic bile duct'),
    ('Cancer of other GI organs; peritoneum', 'Cancer of other GI organs; peritoneum'),
    ('Cancer of other female genital organs', 'Cancer of other female genital organs'),
    ('Cancer of other male genital organs', 'Cancer of other male genital organs'),
    ('Cancer of other urinary organs', 'Cancer of other urinary organs'),
    ('Cancer of ovary', 'Cancer of ovary'),
    ('Cancer of pancreas', 'Cancer of pancreas'),
    ('Cancer of prostate', 'Cancer of prostate'),
    ('Cancer of rectum and anus', 'Cancer of rectum and anus'),
    ('Cancer of stomach', 'Cancer of stomach'),
    ('Cancer of testis', 'Cancer of testis'),
    ('Cancer of thyroid', 'Cancer of thyroid'),
    ('Cancer of uterus', 'Cancer of uterus'),
    ('Cancer; other and unspecified primary', 'Cancer; other and unspecified primary'),
    ('Cancer; other respiratory and intrathoracic', 'Cancer; other respiratory and intrathoracic'),
    ('Cardiac and circulatory congenital anomalies', 'Cardiac and circulatory congenital anomalies'),
    ('Cardiac arrest and ventricular fibrillation', 'Cardiac arrest and ventricular fibrillation'),
    ('Cardiac dysrhythmias', 'Cardiac dysrhythmias'),
    ('Cataract', 'Cataract'),
    ('Chronic kidney disease', 'Chronic kidney disease'),
    ('Chronic obstructive pulmonary disease and bronchiectasis', 'Chronic obstructive pulmonary disease and bronchiectasis'),
    ('Chronic ulcer of skin', 'Chronic ulcer of skin'),
    ('Coagulation and hemorrhagic disorders', 'Coagulation and hemorrhagic disorders'),
    ('Coma; stupor; and brain damage', 'Coma; stupor; and brain damage'),
    ('Complication of device; implant or graft', 'Complication of device; implant or graft'),
    ('Complications of surgical procedures or medical care', 'Complications of surgical procedures or medical care'),
    ('Conditions associated with dizziness or vertigo', 'Conditions associated with dizziness or vertigo'),
    ('Conduction disorders', 'Conduction disorders'),
    ('Congestive heart failure; nonhypertensive', 'Congestive heart failure; nonhypertensive'),
    ('Contraceptive and procreative management', 'Contraceptive and procreative management'),
    ('Coronary atherosclerosis and other heart disease', 'Coronary atherosclerosis and other heart disease'),
    ('Crushing injury or internal injury', 'Crushing injury or internal injury'),
    ('Cystic fibrosis', 'Cystic fibrosis'),
    ('Deficiency and other anemia', 'Deficiency and other anemia'),
    ('Delirium, dementia, and amnestic and other cognitive disorders', 'Delirium, dementia, and amnestic and other cognitive disorders'),
    ('Developmental disorders', 'Developmental disorders'),
    ('Diabetes mellitus with complications', 'Diabetes mellitus with complications'),
    ('Diabetes mellitus without complication', 'Diabetes mellitus without complication'),
    ('Diabetes or abnormal glucose tolerance complicating pregnancy; childbirth; or the puerperium', 'Diabetes or abnormal glucose tolerance complicating pregnancy; childbirth; or the puerperium'),
    ('Digestive congenital anomalies', 'Digestive congenital anomalies'),
    ('Diseases of mouth; excluding dental', 'Diseases of mouth; excluding dental'),
    ('Diseases of white blood cells', 'Diseases of white blood cells'),
    ('Disorders of lipid metabolism', 'Disorders of lipid metabolism'),
    ('Disorders of teeth and jaw', 'Disorders of teeth and jaw'),
    ('Disorders usually diagnosed in infancy, childhood, or adolescence', 'Disorders usually diagnosed in infancy, childhood, or adolescence'),
    ('Diverticulosis and diverticulitis', 'Diverticulosis and diverticulitis'),
    ('E Codes: Adverse effects of medical drugs', 'E Codes: Adverse effects of medical drugs'),
    ('Early or threatened labor', 'Early or threatened labor'),
    ('Encephalitis (except that caused by tuberculosis or sexually transmitted disease)', 'Encephalitis (except that caused by tuberculosis or sexually transmitted disease)'),
    ('Endometriosis', 'Endometriosis'),
    ('Epilepsy; convulsions', 'Epilepsy; convulsions'),
    ('Esophageal disorders', 'Esophageal disorders'),
    ('Essential hypertension', 'Essential hypertension'),
    ('Female infertility', 'Female infertility'),
    ('Fetal distress and abnormal forces of labor', 'Fetal distress and abnormal forces of labor'),
    ('Fetopelvic disproportion; obstruction', 'Fetopelvic disproportion; obstruction'),
    ('Fever of unknown origin', 'Fever of unknown origin'),
    ('Fluid and electrolyte disorders', 'Fluid and electrolyte disorders'),
    ('Forceps delivery', 'Forceps delivery'),
    ('Fracture of lower limb', 'Fracture of lower limb'),
    ('Fracture of neck of femur (hip)', 'Fracture of neck of femur (hip)'),
    ('Fracture of upper limb', 'Fracture of upper limb'),
    ('Gangrene', 'Gangrene'),
    ('Gastritis and duodenitis', 'Gastritis and duodenitis'),
    ('Gastroduodenal ulcer (except hemorrhage)', 'Gastroduodenal ulcer (except hemorrhage)'),
    ('Gastrointestinal hemorrhage', 'Gastrointestinal hemorrhage'),
    ('Genitourinary congenital anomalies', 'Genitourinary congenital anomalies'),
    ('Genitourinary symptoms and ill-defined conditions', 'Genitourinary symptoms and ill-defined conditions'),
    ('Glaucoma', 'Glaucoma'),
    ('Gout and other crystal arthropathies', 'Gout and other crystal arthropathies'),
    ('HIV infection', 'HIV infection'),
    ('Headache; including migraine', 'Headache; including migraine'),
    ('Heart valve disorders', 'Heart valve disorders'),
    ('Hemolytic jaundice and perinatal jaundice', 'Hemolytic jaundice and perinatal jaundice'),
    ('Hemorrhage during pregnancy; abruptio placenta; placenta previa', 'Hemorrhage during pregnancy; abruptio placenta; placenta previa'),
    ('Hemorrhoids', 'Hemorrhoids'),
    ('Hepatitis', 'Hepatitis'),
    ('Hodgkin`s disease', 'Hodgkin`s disease'),
    ('Hyperplasia of prostate', 'Hyperplasia of prostate'),
    ('Hypertension complicating pregnancy; childbirth and the puerperium', 'Hypertension complicating pregnancy; childbirth and the puerperium'),
    ('Hypertension with complications and secondary hypertension', 'Hypertension with complications and secondary hypertension'),
    ('Immunity disorders', 'Immunity disorders'),
    ('Immunizations and screening for infectious disease', 'Immunizations and screening for infectious disease'),
    ('Impulse control disorders, NEC', 'Impulse control disorders, NEC'),
    ('Infective arthritis and osteomyelitis (except that caused by tuberculosis or sexually transmitted disease)', 'Infective arthritis and osteomyelitis (except that caused by tuberculosis or sexually transmitted disease)'),
    ('Inflammation; infection of eye (except that caused by tuberculosis or sexually transmitteddisease)', 'Inflammation; infection of eye (except that caused by tuberculosis or sexually transmitteddisease)'),
    ('Inflammatory conditions of male genital organs', 'Inflammatory conditions of male genital organs'),
    ('Inflammatory diseases of female pelvic organs', 'Inflammatory diseases of female pelvic organs'),
    ('Influenza', 'Influenza'),
    ('Intestinal infection', 'Intestinal infection'),
    ('Intestinal obstruction without hernia', 'Intestinal obstruction without hernia'),
    ('Intracranial injury', 'Intracranial injury'),
    ('Intrauterine hypoxia and birth asphyxia', 'Intrauterine hypoxia and birth asphyxia'),
    ('Joint disorders and dislocations; trauma-related', 'Joint disorders and dislocations; trauma-related'),
    ('Late effects of cerebrovascular disease', 'Late effects of cerebrovascular disease'),
    ('Leukemias', 'Leukemias'),
    ('Liveborn', 'Liveborn'),
    ('Lung disease due to external agents', 'Lung disease due to external agents'),
    ('Lymphadenitis', 'Lymphadenitis'),
    ('Maintenance chemotherapy; radiotherapy', 'Maintenance chemotherapy; radiotherapy'),
    ('Malaise and fatigue', 'Malaise and fatigue'),
    ('Malignant neoplasm without specification of site', 'Malignant neoplasm without specification of site'),
    ('Malposition; malpresentation', 'Malposition; malpresentation'),
    ('Medical examination/evaluation', 'Medical examination/evaluation'),
    ('Melanomas of skin', 'Melanomas of skin'),
    ('Meningitis (except that caused by tuberculosis or sexually transmitted disease)', 'Meningitis (except that caused by tuberculosis or sexually transmitted disease)'),
    ('Menopausal disorders', 'Menopausal disorders'),
    ('Menstrual disorders', 'Menstrual disorders'),
    ('Miscellaneous disorders', 'Miscellaneous disorders'),
    ('Mood disorders', 'Mood disorders'),
    ('Multiple myeloma', 'Multiple myeloma'),
    ('Multiple sclerosis', 'Multiple sclerosis'),
    ('Mycoses', 'Mycoses'),
    ('Nausea and vomiting', 'Nausea and vomiting'),
    ('Neoplasms of unspecified nature or uncertain behavior', 'Neoplasms of unspecified nature or uncertain behavior'),
    ('Nephritis; nephrosis; renal sclerosis', 'Nephritis; nephrosis; renal sclerosis'),
    ('Nervous system congenital anomalies', 'Nervous system congenital anomalies'),
    ('Non-Hodgkin`s lymphoma', 'Non-Hodgkin`s lymphoma'),
    ('Noninfectious gastroenteritis', 'Noninfectious gastroenteritis'),
    ('Nonmalignant breast conditions', 'Nonmalignant breast conditions'),
    ('Nonspecific chest pain', 'Nonspecific chest pain'),
    ('Nutritional deficiencies', 'Nutritional deficiencies'),
    ('OB-related trauma to perineum and vulva', 'OB-related trauma to perineum and vulva'),
    ('Occlusion or stenosis of precerebral arteries', 'Occlusion or stenosis of precerebral arteries'),
    ('Open wounds of extremities', 'Open wounds of extremities'),
    ('Open wounds of head; neck; and trunk', 'Open wounds of head; neck; and trunk'),
    ('Osteoarthritis', 'Osteoarthritis'),
    ('Osteoporosis', 'Osteoporosis'),
    ('Other CNS infection and poliomyelitis', 'Other CNS infection and poliomyelitis'),
    ('Other acquired deformities', 'Other acquired deformities'),
    ('Other aftercare', 'Other aftercare'),
    ('Other and ill-defined cerebrovascular disease', 'Other and ill-defined cerebrovascular disease'),
    ('Other and ill-defined heart disease', 'Other and ill-defined heart disease'),
    ('Other and unspecified benign neoplasm', 'Other and unspecified benign neoplasm'),
    ('Other bone disease and musculoskeletal deformities', 'Other bone disease and musculoskeletal deformities'),
    ('Other circulatory disease', 'Other circulatory disease'),
    ('Other complications of birth; puerperium affecting management of mother', 'Other complications of birth; puerperium affecting management of mother'),
    ('Other complications of pregnancy', 'Other complications of pregnancy'),
    ('Other congenital anomalies', 'Other congenital anomalies'),
    ('Other connective tissue disease', 'Other connective tissue disease'),
    ('Other diseases of bladder and urethra', 'Other diseases of bladder and urethra'),
    ('Other diseases of kidney and ureters', 'Other diseases of kidney and ureters'),
    ('Other diseases of veins and lymphatics', 'Other diseases of veins and lymphatics'),
    ('Other disorders of stomach and duodenum', 'Other disorders of stomach and duodenum'),
    ('Other ear and sense organ disorders', 'Other ear and sense organ disorders'),
    ('Other endocrine disorders', 'Other endocrine disorders'),
    ('Other eye disorders', 'Other eye disorders'),
    ('Other female genital disorders', 'Other female genital disorders'),
    ('Other fractures', 'Other fractures'),
    ('Other gastrointestinal disorders', 'Other gastrointestinal disorders'),
    ('Other hematologic conditions', 'Other hematologic conditions'),
    ('Other hereditary and degenerative nervous system conditions', 'Other hereditary and degenerative nervous system conditions'),
    ('Other infections; including parasitic', 'Other infections; including parasitic'),
    ('Other inflammatory condition of skin', 'Other inflammatory condition of skin'),
    ('Other injuries and conditions due to external causes', 'Other injuries and conditions due to external causes'),
    ('Other liver diseases', 'Other liver diseases'),
    ('Other lower respiratory disease', 'Other lower respiratory disease'),
    ('Other male genital disorders', 'Other male genital disorders'),
    ('Other nervous system disorders', 'Other nervous system disorders'),
    ('Other non-epithelial cancer of skin', 'Other non-epithelial cancer of skin'),
    ('Other non-traumatic joint disorders', 'Other non-traumatic joint disorders'),
    ('Other nutritional; endocrine; and metabolic disorders', 'Other nutritional; endocrine; and metabolic disorders'),
    ('Other perinatal conditions', 'Other perinatal conditions'),
    ('Other pregnancy and delivery including normal', 'Other pregnancy and delivery including normal'),
    ('Other screening for suspected conditions (not mental disorders or infectious disease)', 'Other screening for suspected conditions (not mental disorders or infectious disease)'),
    ('Other skin disorders', 'Other skin disorders'),
    ('Other upper respiratory disease', 'Other upper respiratory disease'),
    ('Other upper respiratory infections', 'Other upper respiratory infections'),
    ('Otitis media and related conditions', 'Otitis media and related conditions'),
    ('Ovarian cyst', 'Ovarian cyst'),
    ('Pancreatic disorders (not diabetes)', 'Pancreatic disorders (not diabetes)'),
    ('Paralysis', 'Paralysis'),
    ('Parkinson`s disease', 'Parkinson`s disease'),
    ('Pathological fracture', 'Pathological fracture'),
    ('Peri-; endo-; and myocarditis; cardiomyopathy (except that caused by tuberculosis or sexually transmitted disease)', 'Peri-; endo-; and myocarditis; cardiomyopathy (except that caused by tuberculosis or sexually transmitted disease)'),
    ('Peripheral and visceral atherosclerosis', 'Peripheral and visceral atherosclerosis'),
    ('Peritonitis and intestinal abscess', 'Peritonitis and intestinal abscess'),
    ('Personality disorders', 'Personality disorders'),
    ('Phlebitis; thrombophlebitis and thromboembolism', 'Phlebitis; thrombophlebitis and thromboembolism'),
    ('Pleurisy; pneumothorax; pulmonary collapse', 'Pleurisy; pneumothorax; pulmonary collapse'),
    ('Pneumonia (except that caused by tuberculosis or sexually transmitted disease)', 'Pneumonia (except that caused by tuberculosis or sexually transmitted disease)'),
    ('Poisoning by nonmedicinal substances', 'Poisoning by nonmedicinal substances'),
    ('Poisoning by other medications and drugs', 'Poisoning by other medications and drugs'),
    ('Poisoning by psychotropic agents', 'Poisoning by psychotropic agents'),
    ('Polyhydramnios and other problems of amniotic cavity', 'Polyhydramnios and other problems of amniotic cavity'),
    ('Previous C-section', 'Previous C-section'),
    ('Prolapse of female genital organs', 'Prolapse of female genital organs'),
    ('Prolonged pregnancy', 'Prolonged pregnancy'),
    ('Pulmonary heart disease', 'Pulmonary heart disease'),
    ('Regional enteritis and ulcerative colitis', 'Regional enteritis and ulcerative colitis'),
    ('Rehabilitation care; fitting of prostheses; and adjustment of devices', 'Rehabilitation care; fitting of prostheses; and adjustment of devices'),
    ('Residual codes; unclassified', 'Residual codes; unclassified'),
    ('Respiratory distress syndrome', 'Respiratory distress syndrome'),
    ('Respiratory failure; insufficiency; arrest (adult)', 'Respiratory failure; insufficiency; arrest (adult)'),
    ('Retinal detachments; defects; vascular occlusion; and retinopathy', 'Retinal detachments; defects; vascular occlusion; and retinopathy'),
    ('Rheumatoid arthritis and related disease', 'Rheumatoid arthritis and related disease'),
    ('Schizophrenia and other psychotic disorders', 'Schizophrenia and other psychotic disorders'),
    ('Screening and history of mental health and substance abuse codes', 'Screening and history of mental health and substance abuse codes'),
    ('Secondary malignancies', 'Secondary malignancies'),
    ('Septicemia (except in labor)', 'Septicemia (except in labor)'),
    ('Sexually transmitted infections (not HIV or hepatitis)', 'Sexually transmitted infections (not HIV or hepatitis)'),
    ('Shock', 'Shock'),
    ('Short gestation; low birth weight; and fetal growth retardation', 'Short gestation; low birth weight; and fetal growth retardation'),
    ('Sickle cell anemia', 'Sickle cell anemia'),
    ('Skin and subcutaneous tissue infections', 'Skin and subcutaneous tissue infections'),
    ('Skull and face fractures', 'Skull and face fractures'),
    ('Spinal cord injury', 'Spinal cord injury'),
    ('Spondylosis; intervertebral disc disorders; other back problems', 'Spondylosis; intervertebral disc disorders; other back problems'),
    ('Sprains and strains', 'Sprains and strains'),
    ('Substance-related disorders', 'Substance-related disorders'),
    ('Suicide and intentional self-inflicted injury', 'Suicide and intentional self-inflicted injury'),
    ('Superficial injury; contusion', 'Superficial injury; contusion'),
    ('Syncope', 'Syncope'),
    ('Systemic lupus erythematosus and connective tissue disorders', 'Systemic lupus erythematosus and connective tissue disorders'),
    ('Thyroid disorders', 'Thyroid disorders'),
    ('Transient cerebral ischemia', 'Transient cerebral ischemia'),
    ('Tuberculosis', 'Tuberculosis'),
    ('Umbilical cord complication', 'Umbilical cord complication'),
    ('Urinary tract infections', 'Urinary tract infections'),
    ('Varicose veins of lower extremity', 'Varicose veins of lower extremity'),
    ('Viral infection', 'Viral infection'),
]
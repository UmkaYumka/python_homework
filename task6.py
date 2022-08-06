goods = []
features = {'название ': '', 'цена ': '', 'количество ': '', 'единица измерения ': ''}
analytics = {'название ': [], 'цена ': [], 'количество ': [], 'единица измерения ': []}
num = 0
feature_ = None
control = None
while True:
    control = input("для выхода нажмите кнопку 'Q', для продолжения 'Ent', для показа аналитики 'E'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'E':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'{f}')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
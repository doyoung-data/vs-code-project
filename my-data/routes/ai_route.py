from flask import render_template, request, jsonify, Blueprint
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

ai_route = Blueprint('ai', __name__)

# 모델 로드
model = tf.keras.models.load_model('C:/Users/do543/vs-code-project/vs-code-project/my-data/cifar10_model.h5')
p_model = tf.keras.models.load_model('C:/Users/do543/vs-code-project/vs-code-project/my-data/pokemon_model_v2.h5')

# CIFAR-10 클래스 이름
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
p_class_names = [
    "abomasnow", "abra", "absol", "accelgor", "aegislash-shield", "aerodactyl", "aggron", "aipom", "alakazam", "alcremie", 
    "alomomola", "altaria", "amaura", "ambipom", "amoonguss", "ampharos", "annihilape", "anorith", "appletun", "applin", 
    "araquanid", "arbok", "arboliva", "arcanine", "arceus", "archen", "archeops", "arctibax", "arctovish", "arctozolt", 
    "ariados", "armaldo", "armarouge", "aromatisse", "aron", "arrokuda", "articuno", "audino", "aurorus", "avalugg", 
    "axew", "azelf", "azumarill", "azurill", "bagon", "baltoy", "banette", "barbaracle", "barboach", "barraskewda", 
    "basculegion-male", "basculin-red-striped", "bastiodon", "baxcalibur", "bayleef", "beartic", "beautifly", "beedrill", 
    "beheeyem", "beldum", "bellibolt", "bellossom", "bellsprout", "bergmite", "bewear", "bibarel", "bidoof", "binacle", 
    "bisharp", "blacephalon", "blastoise", "blaziken", "blipbug", "blissey", "blitzle", "boldore", "boltund", "bombirdier", 
    "bonsly", "bouffalant", "bounsweet", "braixen", "brambleghast", "bramblin", "braviary", "breloom", "brionne", "bronzong", 
    "bronzor", "brute-bonnet", "bruxish", "budew", "buizel", "bulbasaur", "buneary", "bunnelby", "burmy", "butterfree", 
    "buzzwole", "cacnea", "cacturne", "calyrex", "camerupt", "capsakid", "carbink", "carkol", "carnivine", "carracosta", 
    "carvanha", "cascoon", "castform", "caterpie", "celebi", "celesteela", "centiskorch", "ceruledge", "cetitan", "cetoddle", 
    "chandelure", "chansey", "charcadet", "charizard", "charjabug", "charmander", "charmeleon", "chatot", "cherrim", "cherubi", 
    "chesnaught", "chespin", "chewtle", "chikorita", "chimchar", "chimecho", "chinchou", "chingling", "cinccino", "cinderace", 
    "clamperl", "clauncher", "clawitzer", "claydol", "clefable", "clefairy", "cleffa", "clobbopus", "clodsire", "cloyster", 
    "coalossal", "cobalion", "cofagrigus", "combee", "combusken", "comfey", "conkeldurr", "copperajah", "corphish", "corsola", 
    "corviknight", "corvisquire", "cosmoem", "cosmog", "cottonee", "crabominable", "crabrawler", "cradily", "cramorant", 
    "cranidos", "crawdaunt", "cresselia", "croagunk", "crobat", "crocalor", "croconaw", "crustle", "cryogonal", "cubchoo", 
    "cubone", "cufant", "cursola", "cutiefly", "cyclizar", "cyndaquil", "dachsbun", "darkrai", "darmanitan-standard", "dartrix", 
    "darumaka", "decidueye", "dedenne", "deerling", "deino", "delcatty", "delibird", "delphox", "deoxys-normal", "dewgong", 
    "dewott", "dewpider", "dhelmise", "dialga", "diancie", "diggersby", "diglett", "ditto", "dodrio", "doduo", "dolliv", 
    "dondozo", "donphan", "dottler", "doublade", "dracovish", "dracozolt", "dragalge", "dragapult", "dragonair", "dragonite", 
    "drakloak", "drampa", "drapion", "dratini", "drednaw", "dreepy", "drifblim", "drifloon", "drilbur", "drizzile", "drowzee", 
    "druddigon", "dubwool", "ducklett", "dudunsparce-two-segment", "dugtrio", "dunsparce", "duosion", "duraludon", "durant", 
    "dusclops", "dusknoir", "duskull", "dustox", "dwebble", "eelektrik", "eelektross", "eevee", "eiscue-ice", "ekans", "eldegoss", 
    "electabuzz", "electivire", "electrike", "electrode", "elekid", "elgyem", "emboar", "emolga", "empoleon", "enamorus-incarnate", 
    "entei", "escavalier", "espathra", "espeon", "espurr", "eternatus", "excadrill", "exeggcute", "exeggutor", "exploud", "falinks", 
    "farfetchd", "farigiraf", "fearow", "feebas", "fennekin", "feraligatr", "ferroseed", "ferrothorn", "fidough", "finizen", 
    "finneon", "flaaffy", "flabebe", "flamigo", "flapple", "flareon", "fletchinder", "fletchling", "flittle", "floatzel", 
    "floette", "floragato", "florges", "flutter-mane", "flygon", "fomantis", "foongus", "forretress", "fraxure", "frigibax", 
    "frillish", "froakie", "frogadier", "froslass", "frosmoth", "fuecoco", "furfrou", "furret", "gabite", "gallade", "galvantula", 
    "garbodor", "garchomp", "gardevoir", "garganacl", "gastly", "gastrodon", "genesect", "gengar", "geodude", "gholdengo", 
    "gible", "gigalith", "gimmighoul", "girafarig", "giratina-altered", "glaceon", "glalie", "glameow", "glastrier", "gligar", 
    "glimmet", "glimmora", "gliscor", "gloom", "gogoat", "golbat", "goldeen", "golduck", "golem", "golett", "golisopod", 
    "golurk", "goodra", "goomy", "gorebyss", "gossifleur", "gothita", "gothitelle", "gothorita", "gourgeist-average", "grafaiai", 
    "granbull", "grapploct", "graveler", "great-tusk", "greavard", "greedent", "greninja", "grimer", "grimmsnarl", "grookey", 
    "grotle", "groudon", "grovyle", "growlithe", "grubbin", "grumpig", "gulpin", "gumshoos", "gurdurr", "guzzlord", "gyarados", 
    "hakamo-o", "happiny", "hariyama", "hatenna", "hatterene", "hattrem", "haunter", "hawlucha", "haxorus", "heatmor", "heatran", 
    "heliolisk", "helioptile", "heracross", "herdier", "hippopotas", "hippowdon", "hitmonchan", "hitmonlee", "hitmontop", "ho-oh", 
    "honchkrow", "honedge", "hoopa", "hoothoot", "hoppip", "horsea", "houndoom", "houndour", "houndstone", "huntail", "hydreigon", 
    "hypno", "igglybuff", "illumise", "impidimp", "incineroar", "indeedee-male", "infernape", "inkay", "inteleon", "iron-bundle", 
    "iron-hands", "iron-jugulis", "iron-moth", "iron-thorns", "iron-treads", "ivysaur", "jangmo-o", "jellicent", "jigglypuff", 
    "jirachi", "jolteon", "joltik", "jumpluff", "jynx", "kabuto", "kabutops", "kadabra", "kakuna", "kangaskhan", "karrablast", 
    "kartana", "kecleon", "keldeo-ordinary", "kilowattrel", "kingambit", "kingdra", "kingler", "kirlia", "klang", "klawf", 
    "kleavor", "klefki", "klink", "klinklang", "koffing", "komala", "kommo-o", "krabby", "kricketot", "kricketune", "krokorok", 
    "krookodile", "kubfu", "kyogre", "kyurem", "lairon", "lampent", "landorus-incarnate", "lanturn", "lapras","larvesta", 
    "larvitar", "latias", "latios", "leafeon", "leavanny", "lechonk", "ledian", "ledyba",
    "lickilicky", "lickitung", "liepard", "lileep", "lilligant", "lillipup", "linoone", "litleo", "litten", "litwick",
    "lokix", "lombre", "lopunny", "lotad", "loudred", "lucario", "ludicolo", "lugia", "lumineon", "lunala", "lunatone",
    "lurantis", "luvdisc", "luxio", "luxray", "lycanroc-midday", "mabosstiff", "machamp", "machoke", "machop", "magby",
    "magcargo", "magearna", "magikarp", "magmar", "magmortar", "magnemite", "magneton", "magnezone", "makuhita", "malamar",
    "mamoswine", "manaphy", "mandibuzz", "manectric", "mankey", "mantine", "mantyke", "maractus", "mareanie", "mareep",
    "marill", "marowak", "marshadow", "marshtomp", "maschiff", "masquerain", "maushold-family-of-four", "mawile", "medicham",
    "meditite", "meganium", "melmetal", "meloetta-aria", "meltan", "meowscarada", "meowstic-male", "meowth", "mesprit",
    "metagross", "metang", "metapod", "mew", "mewtwo", "mienfoo", "mienshao", "mightyena", "milcery", "milotic", "miltank",
    "mime-jr", "mimikyu-disguised", "minccino", "minior-red-meteor", "minun", "misdreavus", "mismagius", "moltres", "monferno",
    "morelull", "morgrem", "morpeko-full-belly", "mothim", "mr-mime", "mr-rime", "mudbray", "mudkip", "mudsdale", "muk",
    "munchlax", "munna", "murkrow", "musharna", "nacli", "naclstack", "naganadel", "natu", "necrozma", "nickit", "nidoking",
    "nidoqueen", "nidoran-f", "nidoran-m", "nidorina", "nidorino", "nihilego", "nincada", "ninetales", "ninjask", "noctowl",
    "noibat", "noivern", "nosepass", "numel", "nuzleaf", "nymble", "obstagoon", "octillery", "oddish", "oinkologne-male",
    "omanyte", "omastar", "onix", "oranguru", "orbeetle", "oricorio-baile", "orthworm", "oshawott", "overqwil", "pachirisu",
    "palafin-zero", "palkia", "palossand", "palpitoad", "pancham", "pangoro", "panpour", "pansage", "pansear", "paras",
    "parasect", "passimian", "patrat", "pawmi", "pawmo", "pawmot", "pawniard", "pelipper", "perrserker", "persian", "petilil",
    "phanpy", "phantump", "pheromosa", "phione", "pichu", "pidgeot", "pidgeotto", "pidgey", "pidove", "pignite", "pikachu",
    "pikipek", "piloswine", "pincurchin", "pineco", "pinsir", "piplup", "plusle", "poipole", "politoed", "poliwag", "poliwhirl",
    "poliwrath", "polteageist", "ponyta", "poochyena", "popplio", "porygon", "porygon-z", "porygon2", "primarina", "primeape",
    "prinplup", "probopass", "psyduck", "pumpkaboo-average", "pupitar", "purrloin", "purugly", "pyroar", "pyukumuku", "quagsire",
    "quaquaval", "quaxly", "quaxwell", "quilava", "quilladin", "qwilfish", "raboot", "rabsca", "raichu", "raikou", "ralts",
    "rampardos", "rapidash", "raticate", "rattata", "rayquaza", "regice", "regidrago", "regieleki", "regigigas", "regirock",
    "registeel", "relicanth", "rellor", "remoraid", "reshiram", "reuniclus", "revavroom", "rhydon", "rhyhorn", "rhyperior",
    "ribombee", "rillaboom", "riolu", "rockruff", "roggenrola", "rolycoly", "rookidee", "roselia", "roserade", "rotom", "rowlet",
    "rufflet", "runerigus", "sableye", "salamence", "salandit", "salazzle", "samurott", "sandaconda", "sandile", "sandshrew",
    "sandslash", "sandy-shocks", "sandygast", "sawk", "sawsbuck", "scatterbug", "sceptile", "scizor", "scolipede", "scorbunny",
    "scovillain", "scrafty", "scraggy", "scream-tail", "scyther", "seadra", "seaking", "sealeo", "seedot", "seel", "seismitoad",
    "sentret", "serperior", "servine", "seviper", "sewaddle", "sharpedo", "shaymin-land", "shedinja", "shelgon", "shellder",
    "shellos", "shelmet", "shieldon", "shiftry", "shiinotic", "shinx", "shroodle", "shroomish", "shuckle", "shuppet", "sigilyph",
    "silcoon", "silicobra", "silvally", "simipour", "simisage", "simisear", "sinistea", "sirfetchd", "sizzlipede", "skarmory",
    "skeledirge", "skiddo", "skiploom", "skitty", "skorupi", "skrelp", "skuntank", "skwovet", "slaking", "slakoth", "sliggoo",
    "slither-wing", "slowbro", "slowking", "slowpoke", "slugma", "slurpuff", "smeargle", "smoliv", "smoochum", "sneasel",
    "sneasler", "snivy", "snom", "snorlax", "snorunt", "snover", "snubbull", "sobble", "solgaleo", "solosis", "solrock", "spearow",
    "spectrier", "spewpa", "spheal", "spidops", "spinarak", "spinda", "spiritomb", "spoink", "sprigatito", "spritzee",
    "squawkabilly-green-plumage", "squirtle", "stakataka", "stantler", "staraptor", "staravia", "starly", "starmie", "staryu",
    "steelix", "steenee", "stonjourner", "stoutland", "stufful", "stunfisk", "stunky", "sudowoodo", "suicune", "sunflora",
    "sunkern", "surskit", "swablu", "swadloon", "swalot", "swampert", "swanna", "swellow", "swinub", "swirlix", "swoobat",
    "sylveon", "tadbulb", "taillow", "talonflame", "tandemaus", "tangela", "tangrowth", "tapu-bulu", "tapu-fini", "tapu-koko",
    "tapu-lele", "tarountula", "tatsugiri-curly", "tauros", "teddiursa", "tentacool", "tentacruel", "tepig", "terrakion", "thievul",
    "throh", "thundurus-incarnate", "thwackey", "timburr", "tinkatink", "tinkaton", "tinkatuff", "tirtouga", "toedscool",
    "toedscruel", "togedemaru", "togekiss", "togepi", "togetic", "torchic", "torkoal", "tornadus-incarnate", "torracat", "torterra",
    "totodile", "toucannon", "toxapex", "toxel", "toxicroak", "toxtricity-amped", "tranquill", "trapinch", "treecko", "trevenant",
    "tropius", "trubbish", "trumbeak", "tsareena", "turtonator", "turtwig", "tympole", "tynamo", "type-null", "typhlosion",
    "tyranitar", "tyrantrum", "tyrogue", "tyrunt", "umbreon", "unfezant", "unown", "ursaluna", "ursaring", "urshifu-single-strike",
    "uxie", "vanillish", "vanillite", "vanilluxe", "vaporeon", "varoom", "veluza", "venipede", "venomoth", "venonat", "venusaur",
    "vespiquen", "vibrava", "victini", "victreebel", "vigoroth", "vikavolt", "vileplume", "virizion", "vivillon", "volbeat",
    "volcanion", "volcarona", "voltorb", "vullaby", "vulpix", "wailmer", "wailord", "walrein", "wartortle", "watchog", "wattrel",
    "weavile", "weedle", "weepinbell", "weezing", "whimsicott", "whirlipede", "whiscash", "whismur", "wigglytuff", "wiglett",
    "wimpod", "wingull", "wishiwashi-solo", "wobbuffet", "woobat", "wooloo", "wooper", "wormadam-plant", "wugtrio", "wurmple",
    "wynaut", "wyrdeer", "xatu", "xerneas", "xurkitree", "yamask", "yamper", "yanma", "yanmega", "yungoos", "yveltal", "zacian",
    "zamazenta", "zangoose", "zapdos", "zarude", "zebstrika", "zekrom", "zeraora", "zigzagoon", "zoroark", "zorua", "zubat",
    "zweilous", "zygarde-50"
]

# 이미지 전처리 함수 (CIFAR-10 모델에 맞는 크기)
def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(32, 32))  # CIFAR-10 모델에 맞는 크기 (32x32)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가
    mean = 0.4914  # CIFAR-10 데이터셋 평균값
    std = 0.2023   # CIFAR-10 데이터셋 표준편차
    img_array = (img_array - mean) / (std + 1e-7)  # 정규화
    return img_array

# Pokémon 모델 이미지 전처리 함수
def load_and_preprocess_pokemon_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Pokémon 모델에 맞는 크기 (224x224)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가
    img_array = img_array / 255.0  # 정규화
    return img_array

# CIFAR-10 예측 API 라우트
@ai_route.route('/api/ai/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # 이미지 파일 저장
    image_file = request.files['image']
    file_path = os.path.join("uploads", image_file.filename)
    os.makedirs("uploads", exist_ok=True)
    image_file.save(file_path)

    # 이미지 전처리 및 예측
    try:
        preprocessed_img = load_and_preprocess_image(file_path)
        prediction = model.predict(preprocessed_img)

        # 예측된 클래스 및 확률 반환
        predicted_class = prediction.argmax()
        result = {
            "label": class_names[predicted_class],
            "confidence": float(prediction[0][predicted_class])
        }

        # 처리 후 임시 파일 삭제
        os.remove(file_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Pokémon 예측 API 라우트
@ai_route.route('/api/ai/pokemon', methods=['POST'])
def predict_pokemon():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # 이미지 파일 저장
    image_file = request.files['image']
    file_path = os.path.join("uploads", image_file.filename)
    os.makedirs("uploads", exist_ok=True)
    image_file.save(file_path)

    # 이미지 전처리 및 예측
    try:
        preprocessed_img = load_and_preprocess_pokemon_image(file_path)
        prediction = p_model.predict(preprocessed_img)

        # 예측된 클래스 및 확률 반환
        predicted_class = prediction.argmax()
        result = {
            "label": p_class_names[predicted_class],
            "confidence": float(prediction[0][predicted_class])
        }

        # 처리 후 임시 파일 삭제
        os.remove(file_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
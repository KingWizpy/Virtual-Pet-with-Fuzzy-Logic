from asyncio.windows_events import NULL
import time
import pygame

pygame.init()

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("virtual pet")


# image
gambar_panda = pygame.image.load('Assets/Panda_Senang.png')
gambar_panda2 = pygame.image.load('Assets/Panda_Bosan.png')
gambar_panda3 = pygame.image.load('Assets/Panda_Sedih.png')

# Scale
panda = pygame.transform.scale(gambar_panda, (700, 500))
panda2 = pygame.transform.scale(gambar_panda2, (700, 500))
panda3 = pygame.transform.scale(gambar_panda3, (700, 500))

# Musik
pygame.mixer.music.load('Assets/Bgm.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)  #volume 50%

# Fuzzy
def naik(b, a, x):
    if x <= a:
        nilai = 0
    elif x > a and x < b:
        nilai = (x - a) / (b - a)
    elif x >= b:
        nilai = 1
    return nilai

def mid(c, b, a, x):
    if x <= a or x >= c:
        nilai = 0
    elif x >= a and x <= b:
        nilai = (x - a) / (b - a)
    elif x >= b and x <= c:
        nilai = (c - x) / (c - b)
    return nilai

def turun(b, a, x):
    if x <= a:
        nilai = 1
    elif x > a and x < b:
        nilai = (b - x) / (b - a)
    elif x >= b:
        nilai = 0
    return nilai

def inferensi_naik(b, a, alfa):
    nilai = alfa * (b - a) + a
    return nilai

def inferensi_mid(a):
    nilai = 50
    return nilai

def inferensi_turun(b, a, alfa):
    nilai = b - (alfa * (b - a))
    return nilai

#Menampilkan parameter
def draw(a, vardik=None):
    # Set the screen background
    if a == 1:
        screen.blit(panda, (0, 0))
    elif a == 2:
        screen.blit(panda2, (0, 0))
    elif a == 3:
        screen.blit(panda3, (0, 0))

    if vardik:
            # Draw text for selected parameters
            font = pygame.font.Font(None, 24)
            text_y = 100
            for key, value in vardik.items():
                if key in ['emosi']:  # Filter parameters
                    text = font.render(f"{key}: {value}", True, BLACK)
                    screen.blit(text, (620, text_y))
                    text_y += 0
    if vardik:
        # Draw text for selected parameters
        font = pygame.font.Font(None, 24)
        text_x = 270
        text_y = 15
        for key, value in vardik.items():
            if key in ['suhu', 'makan']:  # Filter parameters
                text = font.render(f"{key}: {value}", True, BLACK)
                screen.blit(text, (10, text_y))
                text_y += 20
        for key, value in vardik.items():
            if key in ['kebersihan']:  # Filter parameters
                text = font.render(f"{key}: {value}", True, BLACK)
                screen.blit(text, (10, text_y))
                text_y += 20
        for key, value in vardik.items():
            if key in ['energi', 'kantuk', 'kesehatan']:  # Filter parameters
                text = font.render(f"{value}", True, BLACK)
                text_rect = text.get_rect(topleft=(text_x, text_y))
                screen.blit(text, text_rect)
                text_x += text_rect.width + 55

    pygame.display.update()

        
        
# -------- Main Program Loop -----------


def main():
    # FPS
    FPS = 5
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Limit to 30 frames per second
    clock.tick(FPS)
    # Loop until the user clicks the close button.
    done = False

    # Kurva
    variable = {'energi_naik': 680, 'energi_turun': 380, 'suhu_naik': 23, 'suhu_turun': 17,
                'kebersihan_naik': 68, 'kebersihan_turun': 38, 'makan_naik': 25, 'makan_turun': 15,
                'kantuk_naik': 68, 'kantuk_mid': 50, 'kantuk_turun': 38,
                'kesehatan_naik': 68, 'kesehatan_mid': 50, 'kesehatan_turun': 38,
                'emosi_naik': 80, 'emosi_mid': 50, 'emosi_turun': 20}

    # Variable awal
    energi = 0
    suhu = 0
    kebersihan = 0
    makan = 0
    kantuk = 0
    kesehatan = 0
    emosi = 0

    vardik = {'energi': 480, 'suhu': 20, 'kebersihan': 38,
              'makan': 15, 'kantuk': NULL, 'kesehatan': NULL}

    # Variable yang ditanyakan
    dit1 = 'kantuk'
    dit2 = 'kesehatan'
    dit3 = 'emosi'

    draw(1)

    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Controller__________________________________________________________
        keys_pressed = pygame.key.get_pressed()
        
        # Suhu
        if keys_pressed[pygame.K_1]:
            # Load the music file
            sound_effect = pygame.mixer.Sound('Assets/1.mp3')
            sound_effect.play()
            sound_effect.set_volume(0.2) 
            if vardik['suhu'] < 30:
                newval = int(vardik['suhu']) + 5
                vardik.update({'suhu': newval})
                print("Tingkat suhu +5")
                
        # Makanan
        if keys_pressed[pygame.K_2]:
            sound_effect = pygame.mixer.Sound('Assets/2.mp3')
            sound_effect.play()
            sound_effect.set_volume(0.2) 
            if vardik['makan'] < 40 and vardik['energi'] < 1000:
                newval = int(vardik['makan']) + 10
                newval2 = int(vardik['energi']) + 40
                vardik.update({'makan': newval})
                vardik.update({'energi': newval2})
                print("Tingkat kekenyangan +10, energi+50")

        # Mandi
        if keys_pressed[pygame.K_3]:
            sound_effect = pygame.mixer.Sound('Assets/3.mp3')
            sound_effect.play()
            sound_effect.set_volume(0.2) 
            if vardik['kebersihan'] < 80:
                newval = int(vardik['kebersihan']) + 20
                vardik.update({'kebersihan': newval})
                print("Tingkat kebersihan +20")

        

        # Fuzzifikasi________________________________________________________________
        nk = dict()
        for i in vardik:
            up = naik(variable[i+"_naik"], variable[i+"_turun"], vardik[i])
            nk.update({i+"_naik": up})

            if i == 'kantuk' or i == 'kesehatan' or i == 'emosi':
                middle = mid(
                    variable[i+"_mid"], variable[i+"_naik"], variable[i+"_turun"], vardik[i])
                nk.update({i+"_mid": middle})

            down = turun(variable[i+"_naik"], variable[i+"_turun"], vardik[i])
            nk.update({i+"_turun": down})

        # Inferensi kantuk & Kesehatan___________________________________________________
        alfa = []
        z = []
        sikon = ['naik', 'turun', 'naik']
        alaka = ['energi_', 'suhu_', 'kebersihan_', 'makan_']
        dit = [dit1, dit2]
        for i in range(2):
            for j in range(4):
                if j == 0 or j == 1:
                    kondisi1 = alaka[i+i]+sikon[j]
                    kondisi2 = alaka[i+i+1]+sikon[j]
                    kesimpulan = sikon[j]
                if j == 2 or j == 3:
                    kondisi1 = alaka[i+i]+sikon[j-2]
                    kondisi2 = alaka[i+i+1]+sikon[j-1]
                    kesimpulan = sikon[j-2]

                print("inferensi ke 1", kondisi1, kondisi2, kesimpulan)
                # Fire Strength INTERSEKSI (AND)
                a = min(nk[kondisi1], nk[kondisi2])
                alfa.append(a)
                if(kesimpulan == "turun"):
                    zz = inferensi_turun(
                        variable[dit[i]+"_naik"], variable[dit[i]+"_turun"], a)
                elif(kesimpulan == "naik"):
                    zz = inferensi_naik(
                        variable[dit[i]+"_naik"], variable[dit[i]+"_turun"], a)
                z.append(zz)
                print("Maka nilai ANDnya adalah ", z)

            # DEFUZIFIKASI Kantuk & Kesehatan
            df = 0
            for k in range(len(alfa)):
                df += alfa[k]*z[k]
            defuz = int(df/sum(alfa))
            val = defuz
            if i == 0:
                ver = dit1
                vardik.update({ver: val})
                print("Jadi, nilai ", dit1, " adalah ", defuz)
            else:
                ver = dit2
                vardik.update({ver: val})
                print("Jadi, nilai ", dit2, " adalah ", defuz)
            alfa.clear()
            z.clear()

        # Inferensi emosi________________________________________________________________
        alfa = []
        z = []
        sikon2 = ['naik', 'mid', 'turun', 'mid', 'naik', 'turun', 'naik']

        # update new vardik
        for i in vardik:
            up = naik(variable[i+"_naik"], variable[i+"_turun"], vardik[i])
            nk.update({i+"_naik": up})

            if i == 'kantuk' or i == 'kesehatan' or i == 'emosi':
                middle = mid(
                    variable[i+"_mid"], variable[i+"_naik"], variable[i+"_turun"], vardik[i])
                nk.update({i+"_mid": middle})

            down = turun(variable[i+"_naik"], variable[i+"_turun"], vardik[i])
            nk.update({i+"_turun": down})

        for i in range(9):
            if i <= 2:
                kondisi1 = 'kantuk_'+sikon2[i]
                kondisi2 = 'kesehatan_'+sikon2[i]
                kesimpulan = sikon2[i]
            if i >= 3 and i <= 4:
                kondisi1 = 'kantuk_'+sikon2[i-i+2]
                kondisi2 = 'kesehatan_'+sikon2[i]
                kesimpulan = sikon2[i+2]
            if i >= 5 and i <= 6:
                kondisi1 = 'kantuk_'+sikon2[i-i+1]
                kondisi2 = 'kesehatan_'+sikon2[i]
                kesimpulan = sikon2[i]
            if i >= 7 and i <= 8:
                kondisi1 = 'kantuk_'+sikon2[i-i]
                kondisi2 = 'kesehatan_'+sikon2[i-5]
                kesimpulan = sikon2[i-4]
            print("inferensi ke 2", kondisi1, kondisi2, kesimpulan)
            # Fire Strength INTERSEKSI (AND)
            a = min(nk[kondisi1], nk[kondisi2])
            alfa.append(a)
            if(kesimpulan == "turun"):
                zz = inferensi_turun(
                    variable[dit3+"_naik"], variable[dit3+"_turun"], a)
            elif(kesimpulan == "mid"):
                zz = inferensi_mid(a)
            elif(kesimpulan == "naik"):
                zz = inferensi_naik(
                    variable[dit3+"_naik"], variable[dit3+"_turun"], a)
            z.append(zz)
            print("Maka nilai ANDnya adalah ", z)

        # DEFUZIFIKASI emosi
        df = 0
        for i in range(len(alfa)):
            df += alfa[i]*z[i]

        defuz3 = int(df/sum(alfa))
        ver = dit3
        val = defuz3
        vardik.update({ver: val})
        print("Jadi, nilai ", dit3, " adalah ", defuz3)

        # Hasil Akhir____________________________________________________________________
        print(vardik)
        for key, val in vardik.items():
            if key == 'energi':
                print(key, " : ", val)
            if key == 'suhu':
                print(key, " : ", val)
            if key == 'kebersihan':
                print(key, " : ", val)
            if key == 'makan':
                print(key, " : ", val)
            if key == 'kantuk':
                print(key, " : ", val)
            if key == 'kesehatan':
                print(key, " : ", val)
            if key == 'emosi':
                print(key, " : ", val)
                if val < 38:
                    draw(3)
                elif val < 75 and val > 25:
                    draw(2)
                elif val > 68:
                    draw(1)
            #exec(key + '= val')
        print(nk)
        draw(a, vardik)

        # perubahan parameter
        for i in vardik:
            if i == 'energi':
                if vardik[i] > 0:
                    newval = int(vardik[i]) - 2
                    vardik.update({i: newval})

            elif i == 'suhu':
                if vardik[i] > 10:
                    newval = int(vardik[i]) - 1
                    vardik.update({i: newval})


            elif i == 'kebersihan':
                if vardik[i] > 0:
                    newval = int(vardik[i]) - 1
                    vardik.update({i: newval})

            elif i == 'makan':
                if vardik[i] > 0:
                    newval = int(vardik[i]) - 1
                    vardik.update({i: newval})
        time.sleep(0.2)
    
    pygame.mixer.music.stop()
    pygame.quit()    


if __name__ == "__main__":
    main()

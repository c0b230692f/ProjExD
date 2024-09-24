import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2= pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")  # 練習２
    kk_img = pg.transform.flip(kk_img, True, False)  # 練習２
    kk_rct = kk_img.get_rect()  # 練習8-1：SurfaceからRectを抽出する
    kk_rct.center = 300, 200  # 練習8-2：Rectを使った初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        kk_rct.move_ip((-1,0))
        key_lst = pg.key.get_pressed()  # 練習8-3：キーの押下状態を取得
        if key_lst[pg.K_UP]:  # 上矢印キーがTrueなら
            y=-1
        elif key_lst[pg.K_DOWN]:
            y =+1
        else:
            y =0
        if key_lst[pg.K_LEFT]:
            x=-1
        elif key_lst[pg.K_RIGHT]:
            x=+2
        else:
            x=0
        kk_rct.move_ip((x,y))

        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct)  # 練習４ -> 練習8-5
        pg.display.update()
        tmr += 1        
        clock.tick(400)  # 練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
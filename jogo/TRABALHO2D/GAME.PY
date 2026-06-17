"""
🚀 PLANET EXPLORER
Jogo de exploração espacial em terceira pessoa
Baseado nos assets de planetas do Kenney (kenney.nl) - CC0
"""

import pygame
import math
import random
import sys
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

# ─────────────────────────────────────────────
#  CONSTANTES
# ─────────────────────────────────────────────
SCREEN_W, SCREEN_H = 1280, 720
FPS = 60
TITLE = "🚀 Planet Explorer"

# Paleta inspirada nos assets do Kenney
SKY_BLUE      = (74,  144, 226)
DEEP_SPACE    = (5,   8,   30)
STAR_WHITE    = (255, 255, 255)
NEBULA_PURPLE = (80,  40,  120)
NEBULA_BLUE   = (30,  60,  130)

# Cores dos planetas (baseadas nas imagens)
PLANET_PALETTES = {
    "terra":   [(100, 180, 240), (60, 160, 80),  (220, 230, 240), (40, 130, 60)],
    "marte":   [(200, 80,  50),  (170, 60,  40), (220, 110, 80),  (140, 50, 30)],
    "roxo":    [(140, 80,  220), (100, 50,  180),(160, 100, 240), (80, 40, 160)],
    "marrom":  [(180, 130, 80),  (140, 100, 60), (200, 150, 100),(120, 85, 50)],
    "gelo":    [(200, 220, 255), (160, 190, 230),(230, 240, 255), (140, 170, 210)],
    "lava":    [(220, 60,  20),  (180, 40,  10), (240, 100, 30),  (160, 30, 10)],
    "verde":   [(60,  200, 100), (40,  160, 70), (80,  220, 120), (30, 130, 55)],
    "cinza":   [(150, 150, 160), (120, 120, 130),(170, 170, 180), (100, 100, 110)],
}

PLANET_NAMES = [
    "Arvoria", "Krethon", "Luminar", "Vexaris", "Drathon",
    "Soleth", "Pyraxis", "Glaceon", "Mordeth", "Auronis",
    "Zephyra", "Crathus", "Verdalis", "Igneos", "Umbris",
]

PLANET_DESCRIPTIONS = {
    "terra":  "Planeta oceânico rico em vida. Atmosfera respirável.",
    "marte":  "Deserto vermelho hostil. Tempestades de areia frequentes.",
    "roxo":   "Planeta gasoso com cristais flutuantes. Bela à distância.",
    "marrom": "Terra árida com antigas ruínas de civilizações perdidas.",
    "gelo":   "Superfície congelada. Oceanos subterrâneos abrigam vida.",
    "lava":   "Vulcões ativos cobrem toda a superfície. Extremamente perigoso.",
    "verde":  "Selva densa e exuberante. Fauna e flora desconhecidas.",
    "cinza":  "Asteroide gigante. Minérios raros abundantes.",
}

# ─────────────────────────────────────────────
#  CLASSES DE DADOS
# ─────────────────────────────────────────────
@dataclass
class Star:
    x: float
    y: float
    size: float
    brightness: int
    twinkle_speed: float
    twinkle_offset: float

@dataclass
class Planet:
    name: str
    x: float
    y: float
    radius: int
    palette_key: str
    description: str
    has_ring: bool = False
    has_moon: bool = False
    rotation: float = 0.0
    rotation_speed: float = 0.0
    moon_angle: float = 0.0
    craters: List[Tuple] = field(default_factory=list)
    cloud_patches: List[Tuple] = field(default_factory=list)

@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    life: float
    max_life: float
    color: Tuple
    size: float

# ─────────────────────────────────────────────
#  FUNÇÕES DE DESENHO DE PLANETAS
# ─────────────────────────────────────────────

def draw_planet(surface: pygame.Surface, planet: Planet, cam_x: float, cam_y: float, hover: bool = False):
    """Desenha um planeta estilo Kenney com shading, textura e detalhes."""
    sx = int(planet.x - cam_x)
    sy = int(planet.y - cam_y)
    r = planet.radius
    palette = PLANET_PALETTES[planet.palette_key]

    # Clip — não desenha se fora da tela
    if sx + r < -50 or sx - r > SCREEN_W + 50 or sy + r < -50 or sy - r > SCREEN_H + 50:
        return

    # Sombra
    shadow_surf = pygame.Surface((r * 2 + 20, r * 2 + 20), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow_surf, (0, 0, 0, 60), (10, 16, r * 2, r * 2))
    surface.blit(shadow_surf, (sx - r - 10, sy - r - 10))

    # Anel (antes do planeta)
    if planet.has_ring:
        ring_color = (*palette[0], 100)
        ring_surf = pygame.Surface((r * 3, r), pygame.SRCALPHA)
        pygame.draw.ellipse(ring_surf, ring_color, (0, 0, r * 3, r))
        pygame.draw.ellipse(ring_surf, (0, 0, 0, 0), (r // 2, r // 6, r * 2, r * 2 // 3))
        surface.blit(ring_surf, (sx - r * 3 // 2, sy))

    # Base do planeta
    planet_surf = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)

    # Cor base
    pygame.draw.circle(planet_surf, palette[0], (r, r), r)

    # Manchas de textura (estilo camuflagem do Kenney)
    rng = random.Random(hash(planet.name))
    for _ in range(12):
        cx = rng.randint(r // 4, r * 7 // 4)
        cy = rng.randint(r // 4, r * 7 // 4)
        cr = rng.randint(r // 5, r // 2)
        color = palette[rng.randint(1, len(palette) - 1)]
        pygame.draw.ellipse(planet_surf, color,
                            (cx - cr, cy - cr * 2 // 3, cr * 2, cr * 4 // 3))

    # Aplica máscara circular
    mask = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
    pygame.draw.circle(mask, (255, 255, 255, 255), (r, r), r)
    planet_surf.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    # Craters (planetas rochosos)
    if planet.palette_key in ("cinza", "marrom", "marte", "lava"):
        for cx, cy, cr in planet.craters:
            if (cx - r) ** 2 + (cy - r) ** 2 < (r - cr) ** 2:
                dark = tuple(max(0, c - 40) for c in palette[1])
                pygame.draw.circle(planet_surf, dark, (cx, cy), cr)
                light = tuple(min(255, c + 30) for c in palette[0])
                pygame.draw.circle(planet_surf, light, (cx - cr // 4, cy - cr // 4), max(1, cr // 3))

    # Nuvens (planetas com atmosfera)
    if planet.palette_key in ("terra", "gelo", "verde"):
        for cx, cy, cw, ch in planet.cloud_patches:
            if (cx - r) ** 2 + (cy - r) ** 2 < (r * 0.85) ** 2:
                cloud_color = (240, 245, 255, 160)
                cloud_surf = pygame.Surface((cw, ch), pygame.SRCALPHA)
                pygame.draw.ellipse(cloud_surf, cloud_color, (0, 0, cw, ch))
                planet_surf.blit(cloud_surf, (cx - cw // 2, cy - ch // 2))

    # Shading: escuro na borda esquerda-inferior
    shade_surf = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
    for i in range(r, 0, -5):
        alpha = int(120 * (1 - i / r) ** 1.5)
        pygame.draw.circle(shade_surf, (0, 0, 30, alpha), (r + r // 4, r + r // 4), i)
    planet_surf.blit(shade_surf, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    # Highlight: brilho no canto superior-direito
    hi_surf = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
    highlight_r = r // 3
    pygame.draw.circle(hi_surf, (255, 255, 255, 50), (r - r // 3, r - r // 3), highlight_r)
    planet_surf.blit(hi_surf, (0, 0))

    surface.blit(planet_surf, (sx - r, sy - r))

    # Lua
    if planet.has_moon:
        moon_r = max(6, r // 5)
        mx = sx + int(math.cos(planet.moon_angle) * (r + moon_r + 15))
        my = sy + int(math.sin(planet.moon_angle) * (r + moon_r + 15) * 0.4)
        moon_col = (200, 200, 210)
        pygame.draw.circle(surface, moon_col, (mx, my), moon_r)
        pygame.draw.circle(surface, (160, 160, 170), (mx + moon_r // 4, my + moon_r // 4), moon_r, 1)

    # Glow de hover
    if hover:
        glow = pygame.Surface((r * 2 + 30, r * 2 + 30), pygame.SRCALPHA)
        pygame.draw.circle(glow, (*palette[0], 60), (r + 15, r + 15), r + 12)
        surface.blit(glow, (sx - r - 15, sy - r - 15))

    # Nome do planeta
    if hover or r > 60:
        font = pygame.font.SysFont("arial", max(12, r // 4), bold=True)
        txt = font.render(planet.name, True, (255, 255, 255))
        shadow = font.render(planet.name, True, (0, 0, 0))
        surface.blit(shadow, (sx - txt.get_width() // 2 + 1, sy + r + 7))
        surface.blit(txt, (sx - txt.get_width() // 2, sy + r + 6))


def draw_player(surface: pygame.Surface, x: int, y: int, angle: float, thrust: bool):
    """Desenha a nave do jogador estilo cartoon."""
    ship = pygame.Surface((40, 50), pygame.SRCALPHA)

    # Corpo da nave
    body = [(20, 2), (34, 40), (20, 32), (6, 40)]
    pygame.draw.polygon(ship, (220, 230, 255), body)
    pygame.draw.polygon(ship, (140, 160, 200), body, 2)

    # Janela
    pygame.draw.circle(ship, (100, 200, 255), (20, 16), 7)
    pygame.draw.circle(ship, (200, 240, 255), (17, 13), 3)

    # Asas
    pygame.draw.polygon(ship, (160, 180, 220), [(6, 30), (0, 42), (12, 35)])
    pygame.draw.polygon(ship, (160, 180, 220), [(34, 30), (40, 42), (28, 35)])

    # Motor
    if thrust:
        flame_colors = [(255, 200, 50), (255, 120, 20), (255, 60, 0)]
        for i, fc in enumerate(flame_colors):
            flame_h = random.randint(10, 20) - i * 3
            pygame.draw.ellipse(ship, fc, (14 + i * 2, 40 - i, 12 - i * 4, flame_h))

    # Rotaciona e posiciona
    rotated = pygame.transform.rotate(ship, -math.degrees(angle) - 90)
    rect = rotated.get_rect(center=(x, y))
    surface.blit(rotated, rect)


# ─────────────────────────────────────────────
#  GERADOR DE SISTEMA SOLAR
# ─────────────────────────────────────────────

def generate_solar_system(seed: int = 42) -> List[Planet]:
    rng = random.Random(seed)
    planets = []
    keys = list(PLANET_PALETTES.keys())

    num_planets = 12
    used_names = set()

    for i in range(num_planets):
        # Posição em espiral
        angle = rng.uniform(0, math.pi * 2)
        dist = rng.randint(400, 3000)
        x = math.cos(angle) * dist + 3000
        y = math.sin(angle) * dist + 2000

        radius = rng.randint(55, 160)
        palette_key = rng.choice(keys)

        name = rng.choice(PLANET_NAMES)
        while name in used_names:
            name = rng.choice(PLANET_NAMES)
        used_names.add(name)

        has_ring = rng.random() < 0.25
        has_moon = rng.random() < 0.5

        # Craters
        craters = []
        if palette_key in ("cinza", "marrom", "marte"):
            for _ in range(rng.randint(3, 8)):
                cx = rng.randint(radius // 4, radius * 7 // 4)
                cy = rng.randint(radius // 4, radius * 7 // 4)
                cr = rng.randint(radius // 8, radius // 4)
                craters.append((cx, cy, cr))

        # Clouds
        clouds = []
        if palette_key in ("terra", "gelo", "verde"):
            for _ in range(rng.randint(4, 9)):
                cx = rng.randint(radius // 3, radius * 5 // 3)
                cy = rng.randint(radius // 3, radius * 5 // 3)
                cw = rng.randint(radius // 3, radius * 2 // 3)
                ch = rng.randint(radius // 6, radius // 3)
                clouds.append((cx, cy, cw, ch))

        p = Planet(
            name=name,
            x=x, y=y,
            radius=radius,
            palette_key=palette_key,
            description=PLANET_DESCRIPTIONS[palette_key],
            has_ring=has_ring,
            has_moon=has_moon,
            rotation=rng.uniform(0, math.pi * 2),
            rotation_speed=rng.uniform(0.001, 0.005),
            moon_angle=rng.uniform(0, math.pi * 2),
            craters=craters,
            cloud_patches=clouds,
        )
        planets.append(p)

    return planets


def generate_stars(seed: int = 99) -> List[Star]:
    rng = random.Random(seed)
    stars = []
    for _ in range(800):
        stars.append(Star(
            x=rng.uniform(0, 6000),
            y=rng.uniform(0, 4000),
            size=rng.uniform(0.5, 2.5),
            brightness=rng.randint(150, 255),
            twinkle_speed=rng.uniform(0.02, 0.08),
            twinkle_offset=rng.uniform(0, math.pi * 2),
        ))
    return stars


# ─────────────────────────────────────────────
#  CLASSE PRINCIPAL DO JOGO
# ─────────────────────────────────────────────

class PlanetExplorer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        # Fontes
        self.font_big   = pygame.font.SysFont("arial", 32, bold=True)
        self.font_med   = pygame.font.SysFont("arial", 20, bold=True)
        self.font_small = pygame.font.SysFont("arial", 14)
        self.font_hud   = pygame.font.SysFont("consolas", 16, bold=True)

        # Mundo
        self.planets = generate_solar_system(seed=7)
        self.stars   = generate_stars(seed=13)
        self.particles: List[Particle] = []

        # Nave (jogador)
        self.px = 3000.0
        self.py = 2000.0
        self.vx = 0.0
        self.vy = 0.0
        self.angle = 0.0  # radianos
        self.speed_max = 6.0
        self.thrust_power = 0.18
        self.friction = 0.985

        # Câmera
        self.cam_x = self.px - SCREEN_W // 2
        self.cam_y = self.py - SCREEN_H // 2

        # Estado
        self.visited_planets: set = set()
        self.selected_planet: Optional[Planet] = None
        self.exploring_planet: Optional[Planet] = None
        self.exploration_progress = 0.0
        self.fuel = 100.0
        self.score = 0
        self.time_elapsed = 0
        self.show_map = False
        self.show_help = True
        self.help_timer = 180

        # Nebulosas (decoração do fundo)
        rng = random.Random(55)
        self.nebulae = [
            (rng.randint(0, 6000), rng.randint(0, 4000),
             rng.randint(300, 700), rng.randint(200, 500),
             rng.choice([(80, 40, 120, 30), (30, 60, 130, 25), (20, 80, 100, 20)]))
            for _ in range(8)
        ]

    # ── UPDATE ────────────────────────────────

    def update(self):
        self.time_elapsed += 1
        keys = pygame.key.get_pressed()

        if not self.exploring_planet:
            self._handle_ship(keys)

        self._update_planets()
        self._update_particles()
        self._update_camera()
        self._check_planet_proximity()

        if self.exploring_planet:
            self._update_exploration(keys)

        if self.help_timer > 0:
            self.help_timer -= 1

    def _handle_ship(self, keys):
        # Rotação
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += 0.05

        # Empuxo
        thrusting = (keys[pygame.K_UP] or keys[pygame.K_w]) and self.fuel > 0
        if thrusting:
            self.vx += math.cos(self.angle) * self.thrust_power
            self.vy += math.sin(self.angle) * self.thrust_power
            self.fuel = max(0, self.fuel - 0.05)
            # Partículas do motor
            if random.random() < 0.5:
                back_angle = self.angle + math.pi
                self.particles.append(Particle(
                    x=self.px + math.cos(back_angle) * 18,
                    y=self.py + math.sin(back_angle) * 18,
                    vx=math.cos(back_angle) * random.uniform(1, 3) + self.vx * 0.3,
                    vy=math.sin(back_angle) * random.uniform(1, 3) + self.vy * 0.3,
                    life=1.0, max_life=1.0,
                    color=random.choice([(255, 180, 40), (255, 100, 20), (255, 220, 100)]),
                    size=random.uniform(2, 5),
                ))

        # Freio
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vx *= 0.93
            self.vy *= 0.93

        # Física
        speed = math.hypot(self.vx, self.vy)
        if speed > self.speed_max:
            self.vx = self.vx / speed * self.speed_max
            self.vy = self.vy / speed * self.speed_max

        self.vx *= self.friction
        self.vy *= self.friction
        self.px += self.vx
        self.py += self.vy

        # Regenera combustível lentamente
        self.fuel = min(100, self.fuel + 0.008)

    def _update_planets(self):
        for p in self.planets:
            p.moon_angle += 0.01

    def _update_particles(self):
        for part in self.particles[:]:
            part.x += part.vx
            part.y += part.vy
            part.vx *= 0.95
            part.vy *= 0.95
            part.life -= 0.03
            if part.life <= 0:
                self.particles.remove(part)

    def _update_camera(self):
        target_cx = self.px - SCREEN_W // 2
        target_cy = self.py - SCREEN_H // 2
        self.cam_x += (target_cx - self.cam_x) * 0.08
        self.cam_y += (target_cy - self.cam_y) * 0.08

    def _check_planet_proximity(self):
        self.selected_planet = None
        for p in self.planets:
            dist = math.hypot(self.px - p.x, self.py - p.y)
            if dist < p.radius + 80:
                self.selected_planet = p
                break

    def _update_exploration(self, keys):
        if keys[pygame.K_e] or keys[pygame.K_RETURN]:
            self.exploration_progress += 0.005
            if self.exploration_progress >= 1.0:
                self._complete_exploration()
        else:
            self.exploration_progress = max(0, self.exploration_progress - 0.002)

    def _complete_exploration(self):
        p = self.exploring_planet
        if p and p.name not in self.visited_planets:
            self.visited_planets.add(p.name)
            self.score += 100 + p.radius
        self.exploring_planet = None
        self.exploration_progress = 0.0

    # ── DRAW ─────────────────────────────────

    def draw(self):
        self.screen.fill(DEEP_SPACE)
        self._draw_nebulae()
        self._draw_stars()
        self._draw_planets()
        self._draw_particles()
        self._draw_player()
        self._draw_hud()
        if self.show_map:
            self._draw_minimap()
        if self.selected_planet and not self.exploring_planet:
            self._draw_planet_info(self.selected_planet)
        if self.exploring_planet:
            self._draw_exploration_ui()
        if self.help_timer > 0:
            self._draw_help()
        pygame.display.flip()

    def _draw_nebulae(self):
        for nx, ny, nw, nh, nc in self.nebulae:
            sx = int(nx - self.cam_x * 0.3)  # parallax
            sy = int(ny - self.cam_y * 0.3)
            neb = pygame.Surface((nw, nh), pygame.SRCALPHA)
            pygame.draw.ellipse(neb, nc, (0, 0, nw, nh))
            self.screen.blit(neb, (sx - nw // 2, sy - nh // 2))

    def _draw_stars(self):
        t = self.time_elapsed / FPS
        for star in self.stars:
            sx = int(star.x - self.cam_x * 0.1) % SCREEN_W
            sy = int(star.y - self.cam_y * 0.1) % SCREEN_H
            twinkle = math.sin(t * star.twinkle_speed * math.pi * 2 + star.twinkle_offset)
            alpha = int(star.brightness * (0.7 + 0.3 * twinkle))
            alpha = max(80, min(255, alpha))
            col = (alpha, alpha, min(255, alpha + 20))
            r = max(1, int(star.size * (0.8 + 0.2 * twinkle)))
            if r == 1:
                self.screen.set_at((sx, sy), col)
            else:
                pygame.draw.circle(self.screen, col, (sx, sy), r)

    def _draw_planets(self):
        keys = pygame.key.get_pressed()
        thrusting = keys[pygame.K_UP] or keys[pygame.K_w]
        _ = thrusting  # usado no player
        for p in self.planets:
            hover = (p == self.selected_planet)
            draw_planet(self.screen, p, self.cam_x, self.cam_y, hover)

    def _draw_particles(self):
        for part in self.particles:
            sx = int(part.x - self.cam_x)
            sy = int(part.y - self.cam_y)
            alpha = int(255 * part.life)
            size = max(1, int(part.size * part.life))
            r, g, b = part.color
            col = (min(255, r), min(255, g), min(255, b))
            pygame.draw.circle(self.screen, col, (sx, sy), size)

    def _draw_player(self):
        keys = pygame.key.get_pressed()
        thrusting = (keys[pygame.K_UP] or keys[pygame.K_w]) and self.fuel > 0
        sx = int(self.px - self.cam_x)
        sy = int(self.py - self.cam_y)
        draw_player(self.screen, sx, sy, self.angle, thrusting)

    def _draw_hud(self):
        # Painel superior
        hud_surf = pygame.Surface((320, 80), pygame.SRCALPHA)
        pygame.draw.rect(hud_surf, (0, 0, 0, 140), (0, 0, 320, 80), border_radius=10)
        self.screen.blit(hud_surf, (10, 10))

        # Combustível
        self._draw_bar(30, 25, 180, 14, self.fuel / 100,
                       (50, 200, 100), (200, 50, 50), "COMBUSTÍVEL")

        # Score
        sc_txt = self.font_hud.render(f"PONTOS: {self.score}", True, (220, 220, 100))
        self.screen.blit(sc_txt, (20, 48))

        # Planetas visitados
        vis_txt = self.font_hud.render(
            f"EXPLORADOS: {len(self.visited_planets)}/{len(self.planets)}", True, (150, 200, 255))
        self.screen.blit(vis_txt, (20, 66))

        # Velocidade
        speed = math.hypot(self.vx, self.vy)
        spd_txt = self.font_small.render(f"VEL: {speed:.1f}", True, (180, 180, 200))
        self.screen.blit(spd_txt, (220, 48))

        # Coord
        coord_txt = self.font_small.render(
            f"X:{int(self.px)} Y:{int(self.py)}", True, (120, 120, 140))
        self.screen.blit(coord_txt, (220, 66))

    def _draw_bar(self, x, y, w, h, pct, col_full, col_empty, label):
        bg = pygame.Surface((w + 60, h + 4), pygame.SRCALPHA)
        pygame.draw.rect(bg, (40, 40, 60, 180), (0, 0, w + 60, h + 4), border_radius=4)
        self.screen.blit(bg, (x - 2, y - 2))

        fill_w = int(w * pct)
        col = (
            int(col_full[0] * pct + col_empty[0] * (1 - pct)),
            int(col_full[1] * pct + col_empty[1] * (1 - pct)),
            int(col_full[2] * pct + col_empty[2] * (1 - pct)),
        )
        pygame.draw.rect(self.screen, col, (x, y, fill_w, h), border_radius=3)
        pygame.draw.rect(self.screen, (200, 200, 220), (x, y, w, h), 1, border_radius=3)

        lbl = self.font_small.render(label, True, (200, 200, 220))
        self.screen.blit(lbl, (x + w + 5, y))

    def _draw_planet_info(self, planet: Planet):
        panel_w, panel_h = 340, 110
        px_screen = SCREEN_W // 2 + 50
        py_screen = SCREEN_H - panel_h - 20

        panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        pygame.draw.rect(panel, (0, 0, 0, 170), (0, 0, panel_w, panel_h), border_radius=12)
        pygame.draw.rect(panel, (100, 150, 255, 200), (0, 0, panel_w, panel_h), 2, border_radius=12)
        self.screen.blit(panel, (px_screen, py_screen))

        name_txt = self.font_med.render(f"🌍 {planet.name}", True, (255, 230, 100))
        self.screen.blit(name_txt, (px_screen + 12, py_screen + 10))

        type_txt = self.font_small.render(
            f"Tipo: {planet.palette_key.capitalize()} | Ø {planet.radius * 2}km",
            True, (170, 200, 255))
        self.screen.blit(type_txt, (px_screen + 12, py_screen + 36))

        desc = self.font_small.render(planet.description[:52] + "...", True, (200, 200, 200))
        self.screen.blit(desc, (px_screen + 12, py_screen + 56))

        if planet.name in self.visited_planets:
            status = self.font_small.render("✅ JÁ EXPLORADO", True, (80, 220, 80))
        else:
            status = self.font_small.render("[ E ] Explorar planeta", True, (255, 200, 50))
        self.screen.blit(status, (px_screen + 12, py_screen + 80))

    def _draw_exploration_ui(self):
        p = self.exploring_planet
        if not p:
            return
        cx, cy = SCREEN_W // 2, SCREEN_H // 2

        # Overlay
        ov = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        pygame.draw.rect(ov, (0, 0, 0, 100), (0, 0, SCREEN_W, SCREEN_H))
        self.screen.blit(ov, (0, 0))

        # Painel de exploração
        pw, ph = 440, 200
        px2 = cx - pw // 2
        py2 = cy - ph // 2 + 80
        panel = pygame.Surface((pw, ph), pygame.SRCALPHA)
        pygame.draw.rect(panel, (10, 20, 50, 220), (0, 0, pw, ph), border_radius=16)
        pygame.draw.rect(panel, (80, 140, 255, 200), (0, 0, pw, ph), 2, border_radius=16)
        self.screen.blit(panel, (px2, py2))

        title = self.font_big.render(f"Explorando: {p.name}", True, (255, 230, 80))
        self.screen.blit(title, (px2 + pw // 2 - title.get_width() // 2, py2 + 14))

        desc = self.font_small.render(p.description, True, (200, 220, 255))
        self.screen.blit(desc, (px2 + pw // 2 - desc.get_width() // 2, py2 + 54))

        # Barra de progresso
        bar_x, bar_y = px2 + 30, py2 + 90
        bar_w = pw - 60
        self._draw_bar(bar_x, bar_y, bar_w, 20,
                       self.exploration_progress, (50, 200, 100), (200, 80, 50), "")
        prog_lbl = self.font_med.render(
            f"Progresso: {int(self.exploration_progress * 100)}%", True, (200, 240, 200))
        self.screen.blit(prog_lbl, (px2 + pw // 2 - prog_lbl.get_width() // 2, py2 + 116))

        hint = self.font_small.render("Segure [E] para explorar  |  [ESC] para sair", True, (160, 160, 190))
        self.screen.blit(hint, (px2 + pw // 2 - hint.get_width() // 2, py2 + 150))

    def _draw_minimap(self):
        mw, mh = 200, 150
        mx, my = SCREEN_W - mw - 10, 10
        mini = pygame.Surface((mw, mh), pygame.SRCALPHA)
        pygame.draw.rect(mini, (0, 0, 0, 180), (0, 0, mw, mh), border_radius=8)
        pygame.draw.rect(mini, (80, 80, 120), (0, 0, mw, mh), 1, border_radius=8)

        world_w, world_h = 6000, 4000
        for p in self.planets:
            pmx = int(p.x / world_w * mw)
            pmy = int(p.y / world_h * mh)
            col = PLANET_PALETTES[p.palette_key][0]
            pr = max(3, p.radius // 20)
            if p.name in self.visited_planets:
                pygame.draw.circle(mini, col, (pmx, pmy), pr)
            else:
                pygame.draw.circle(mini, (100, 100, 100), (pmx, pmy), pr)

        # Jogador no mapa
        pmx = int(self.px / world_w * mw)
        pmy = int(self.py / world_h * mh)
        pygame.draw.circle(mini, (255, 255, 100), (pmx, pmy), 3)

        self.screen.blit(mini, (mx, my))
        lbl = self.font_small.render("MAPA [M]", True, (180, 180, 220))
        self.screen.blit(lbl, (mx + 4, my + mh - 18))

    def _draw_help(self):
        alpha = min(255, self.help_timer * 4)
        lines = [
            "CONTROLES:",
            "W / ↑  — Acelerar",
            "A/D / ←→  — Girar",
            "S / ↓  — Frear",
            "E / Enter — Explorar planeta",
            "M — Mapa",
            "ESC — Sair",
        ]
        help_surf = pygame.Surface((220, 160), pygame.SRCALPHA)
        pygame.draw.rect(help_surf, (0, 0, 0, int(160 * alpha / 255)),
                         (0, 0, 220, 160), border_radius=10)
        self.screen.blit(help_surf, (SCREEN_W - 240, SCREEN_H - 180))
        for i, line in enumerate(lines):
            col = (255, 230, 100) if i == 0 else (180, 200, 255)
            txt = self.font_small.render(line, True, col)
            txt.set_alpha(alpha)
            self.screen.blit(txt, (SCREEN_W - 232, SCREEN_H - 168 + i * 20))

    # ── EVENTOS ──────────────────────────────

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.exploring_planet:
                        self.exploring_planet = None
                        self.exploration_progress = 0
                    else:
                        return False
                if event.key == pygame.K_m:
                    self.show_map = not self.show_map
                if event.key in (pygame.K_e, pygame.K_RETURN):
                    if self.selected_planet and not self.exploring_planet:
                        self.exploring_planet = self.selected_planet
                        self.exploration_progress = 0.0
        return True

    # ── LOOP PRINCIPAL ────────────────────────

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


# ─────────────────────────────────────────────
#  TELA DE TÍTULO
# ─────────────────────────────────────────────

def draw_title_screen(screen, clock, stars, planets):
    font_title = pygame.font.SysFont("arial", 72, bold=True)
    font_sub   = pygame.font.SysFont("arial", 26)
    font_hint  = pygame.font.SysFont("arial", 20)
    t = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

        screen.fill(DEEP_SPACE)

        # Estrelas
        for star in stars[:300]:
            sx = int(star.x / 6000 * SCREEN_W)
            sy = int(star.y / 4000 * SCREEN_H)
            twinkle = math.sin(t * star.twinkle_speed * 0.5 + star.twinkle_offset)
            b = int(star.brightness * (0.7 + 0.3 * twinkle))
            pygame.draw.circle(screen, (b, b, min(255, b + 20)), (sx, sy), max(1, int(star.size)))

        # Planetas decorativos ao fundo
        dec_positions = [(200, 200, 80), (1000, 400, 60), (600, 550, 50), (1100, 150, 70)]
        for i, (dx, dy, dr) in enumerate(dec_positions):
            p = planets[i % len(planets)]
            p2 = Planet(
                name="", x=dx + SCREEN_W // 2 - 640, y=dy,
                radius=dr, palette_key=p.palette_key,
                description="", has_ring=p.has_ring, has_moon=False,
                craters=p.craters[:3], cloud_patches=p.cloud_patches[:3],
                moon_angle=p.moon_angle,
            )
            draw_planet(screen, p2, 0, 0)

        # Título com glow
        pulse = 0.85 + 0.15 * math.sin(t * 0.05)
        glow_col = (int(50 * pulse), int(80 * pulse), int(200 * pulse))
        for offset in [(3, 3), (-3, -3), (3, -3), (-3, 3)]:
            glow_txt = font_title.render("PLANET EXPLORER", True, glow_col)
            screen.blit(glow_txt, (SCREEN_W // 2 - glow_txt.get_width() // 2 + offset[0],
                                   SCREEN_H // 2 - 120 + offset[1]))
        title_txt = font_title.render("PLANET EXPLORER", True, (220, 240, 255))
        screen.blit(title_txt, (SCREEN_W // 2 - title_txt.get_width() // 2, SCREEN_H // 2 - 120))

        sub_txt = font_sub.render("Explore planetas desconhecidos pelo universo", True, (160, 190, 255))
        screen.blit(sub_txt, (SCREEN_W // 2 - sub_txt.get_width() // 2, SCREEN_H // 2 - 30))

        blink = int(200 * (0.6 + 0.4 * math.sin(t * 0.1)))
        hint = font_hint.render("Pressione ENTER para iniciar", True, (blink, blink, 100))
        screen.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H // 2 + 40))

        credit = font_hint.render("Assets: Kenney (kenney.nl) — CC0", True, (100, 100, 130))
        screen.blit(credit, (SCREEN_W // 2 - credit.get_width() // 2, SCREEN_H - 30))

        pygame.display.flip()
        clock.tick(FPS)
        t += 1


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    stars   = generate_stars()
    planets = generate_solar_system()

    draw_title_screen(screen, clock, stars, planets)

    game = PlanetExplorer()
    game.run()
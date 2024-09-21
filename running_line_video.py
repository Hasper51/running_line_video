import cv2
import numpy as np

# Функция для создания видео с бегущей строкой
def create_text_video_opencv():
    # Текст для вывода
    message = "Hello World"

    # Параметры видео
    width, height = 100, 100  # Разрешение видео
    fps = 24  # Кадров в секунду
    video_length = 3  # Длительность видео в секундах

    # Рассчитаем общее количество кадров
    total_frames = video_length * fps

    # Настройка видеопотока
    out = cv2.VideoWriter("hello_world.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Создаем кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Настройки шрифта
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)  # Белый цвет текста

    # Получаем размер текста
    (text_width, text_height), _ = cv2.getTextSize(message, font, font_scale, font_thickness)

    # Рассчитываем начальную позицию и скорость текста
    x_start = width  # Начинаем с правого края экрана
    x_end = -text_width  # Заканчиваем, когда текст полностью выйдет за левый край

    # Рассчитываем общее расстояние, которое должен пройти текст, и скорость за кадр
    total_distance = x_start - x_end
    speed_per_frame = total_distance / total_frames

    # Вертикальная позиция для текста (по центру вертикали)
    y = height // 2 + text_height // 2

    # Проходим по каждому кадру
    for t in range(total_frames):
        # Очищаем кадр (черный фон)
        frame.fill(0)

        # Рассчитываем новую координату x для текста
        x = int(x_start - t * speed_per_frame)

        # Отображаем текст на кадре
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)

        # Записываем кадр в видео
        out.write(frame)

    # Освобождаем видеопоток
    out.release()

# Создаем видео
create_text_video_opencv()

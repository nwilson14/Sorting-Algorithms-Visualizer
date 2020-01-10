# Merge Sort
# Quick Sort
# Heap Sort - done
# Bubble Sort - DONE DONE DONE
# Selection Sort - DONE DONE DONE
# Add Insertion Sort

# Author: Noah Wilson, wilsonn2018@my.fit.edu
# Description: This program contains six sorting algorithms and
#              and visualizes them. (The algorithms sorts them in
#              increasing order)

from sys import stdin, stdout
import pygame
from pygame.locals import *


class Button:
    def __init__(self, color, position, dimensions, caption):
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.length = dimensions[0]
        self.width = dimensions[1]
        self.caption = caption

    # This function draws the rectangle button
    def draw(self, display, outline=None):
        if outline:
            pygame.draw.rect(display, outline, (self.x-2, self.y-2, self.width+4, self.length+4), 0)
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.length), 0)

        if self.caption != " " or self.caption.isdigit():
            font = pygame.font.SysFont("bahnschrift", 18, bold=True)
            caption = font.render(self.caption, 1, (0, 0, 0))
            display.blit(caption, (self.x + 5, self.y + 5))

    # This function returns whether the mouse is over the button
    def check_mouse_pos(self, pos):
        if self.x < pos[0] < (self.x + self.width):
            if self.y < pos[1] < (self.y + self.length):
                return True
        return False

    # This function swaps the position of two buttons
    def swap(self, display, button2):
        black1 = Button((0, 0, 0), (self.x, self.y),
                        (self.length, self.width), " ")
        black2 = Button((0, 0, 0), (button2.x, button2.y),
                        (button2.length, button2.width), " ")
        black1.draw(display)
        black2.draw(display)
        temp_x = self.x
        self.x = button2.x
        button2.x = temp_x
        temp_y = self.y
        self.y = button2.y
        button2.y = temp_y
        self.draw(display)
        button2.draw(display)

        self.color = (180, 255, 100)
        self.draw(display)

        pygame.display.update()

# ----------- End of Class definition ----------- #


def sorting_screen(screen, array):
    screen.fill((0, 0, 0))
    separation = 50
    b_list = list()
    for k in range(len(array)):
        new_b = Button((180, 255, 100), (separation, 0), (array[k] * 5, 5), str(array[k]))
        new_b.draw(screen)
        b_list.append(new_b)
        separation += 6
    play_b = Button((180, 255, 100), (50, 550), (35, 65), "Go!")
    play_b.draw(screen)
    back_b = Button((180, 255, 100), (600, 550), (35, 65), "Back")
    back_b.draw(screen)
    sorting_b = Button((180, 255, 100), (50, 550), (35, 65), "Sorting...")
    button_list = [play_b, back_b, sorting_b]
    pygame.display.update()
    return screen, button_list, b_list


def bubble_sort(array, screen, button_list, rectangle_list):
    """Bubble sort: Time Complexity: O(n^2). Compare sequential items and swap them
        if one is greater than the other"""
    # Create a new display with bars to sort
    # Create a list of all the
    comparisons = 0
    font = pygame.font.SysFont("bahnschrift", 20)
    play_b = button_list[0]
    back_b = button_list[1]
    while True:
        pygame.display.update()
        for user_input in pygame.event.get():
            if user_input.type == QUIT:
                pygame.quit()
                quit()

            mouse = pygame.mouse.get_pos()
            if user_input.type == MOUSEBUTTONDOWN:
                if play_b.check_mouse_pos(mouse):
                    play_b = Button((180, 255, 100), (50, 550), (35, 100), "Sorting...")
                    play_b.draw(screen)
                    for i in range(len(array)):
                        for j in range(len(array)-i-1):
                            # Change color of bars being compared
                            rectangle_list[j].color = (255, 100, 100)
                            rectangle_list[j].draw(screen)
                            rectangle_list[j + 1].color = (255, 100, 100)
                            rectangle_list[j + 1].draw(screen)
                            # Update comparisons
                            comp_text = font.render("Comparisons: " + str(comparisons), False, (0, 0, 0))
                            screen.blit(comp_text, (250, 550))
                            comparisons += 1
                            comp_text = font.render("Comparisons: " + str(comparisons), False, (255, 255, 255))
                            screen.blit(comp_text, (250, 550))
                            if array[j] > array[j+1]:
                                # Swapping the physical bars
                                rectangle_list[j].swap(screen, rectangle_list[j+1])
                                # Swapping positions in the button array
                                t = rectangle_list[j]
                                rectangle_list[j] = rectangle_list[j+1]
                                rectangle_list[j+1] = t
                                # Swapping the positions in the actual array
                                temp = array[j]
                                array[j] = array[j+1]
                                array[j+1] = temp
                            # Update color back to normal
                            rectangle_list[j].color = (180, 255, 100)
                            rectangle_list[j].draw(screen)
                            rectangle_list[j + 1].color = (180, 255, 100)
                            rectangle_list[j + 1].draw(screen)
                    done_b = Button((180, 255, 100), (50, 550), (35, 100), "Done!")
                    done_b.draw(screen)
                    pygame.display.update()
                elif back_b.check_mouse_pos(mouse):
                    main()

# ----------- End of Bubble Sort function ----------- #


def merge(array):
    """Combining the single element arrays and other arrays"""


def merge_sort(array, screen, button_list, rectangle_list):
    """Merge Sort: Time Complexity O(nlogn)"""
    stdout.write("Merge Sort\n")
    play_b = button_list[0]
    back_b = button_list[1]
    comparisons = 0
    font = pygame.font.SysFont("bahnschrift", 20)
    while True:
        pygame.display.update()
        for user_input in pygame.event.get():
            if user_input.type == QUIT:
                pygame.quit()
                quit()

            mouse = pygame.mouse.get_pos()
            if user_input.type == MOUSEBUTTONDOWN:
                if play_b.check_mouse_pos(mouse):
                    play_b = Button((180, 255, 100), (50, 550), (35, 100), "Sorting...")
                    play_b.draw(screen)
                    # Sorting algorithm goes here
                    done_b = Button((180, 255, 100), (50, 550), (35, 100), "Done!")
                    done_b.draw(screen)
                    pygame.display.update()
                elif back_b.check_mouse_pos(mouse):
                    main()

# ----------- End of Merge Sort function ----------- #


def selection_sort(array, screen, button_list, rectangle_list):
    """Selection Sort: Time Complexity: O(n^2). Start with first item, set as minimum.
        If an item is found that is smaller than the minimum, switch those items."""
    stdout.write("Selection Sort\n")
    play_b = button_list[0]
    back_b = button_list[1]
    comparisons = 0
    font = pygame.font.SysFont("bahnschrift", 20)
    while True:
        pygame.display.update()
        for user_input in pygame.event.get():
            if user_input.type == QUIT:
                pygame.quit()
                quit()

            mouse = pygame.mouse.get_pos()
            if user_input.type == MOUSEBUTTONDOWN:
                if play_b.check_mouse_pos(mouse):
                    play_b = Button((180, 255, 100), (50, 550), (35, 100), "Sorting...")
                    play_b.draw(screen)
                    for i in range(len(array)):
                        min_num = i
                        for j in range(i, len(array)):
                            # Change color of bars being compared
                            # Update comparisons and display it on screen
                            comp_text = font.render("Comparisons: " + str(comparisons), False, (0, 0, 0))
                            screen.blit(comp_text, (250, 550))
                            comparisons += 1
                            comp_text = font.render("Comparisons: " + str(comparisons), False, (255, 255, 255))
                            screen.blit(comp_text, (250, 550))
                            # Perform comparison
                            if array[j] <= array[min_num]:
                                min_num = j
                        # Swapping the physical bars on screen
                        rectangle_list[i].swap(screen, rectangle_list[min_num])
                        # Swapping positions in the bar array
                        t = rectangle_list[i]
                        rectangle_list[i] = rectangle_list[min_num]
                        rectangle_list[min_num] = t
                        # Swapping positions on the array
                        temp = array[i]
                        array[i] = array[min_num]
                        array[min_num] = temp
                    done_b = Button((180, 255, 100), (50, 550), (35, 100), "Done!")
                    done_b.draw(screen)
                    pygame.display.update()
                elif back_b.check_mouse_pos(mouse):
                    main()

# ----------- End of Selection Sort function ----------- #


def quick_sort(array, screen, button_list, rectangle_list):
    """Quick Sort: Time Complexity: BC - O(nlogn) WC - O(n^2)"""
    stdout.write("Quick Sort\n")
    play_b = button_list[0]
    back_b = button_list[1]
    comparisons = 0
    font = pygame.font.SysFont("bahnschrift", 20)
    while True:
        pygame.display.update()
        for user_input in pygame.event.get():
            if user_input.type == QUIT:
                pygame.quit()
                quit()

            mouse = pygame.mouse.get_pos()
            if user_input.type == MOUSEBUTTONDOWN:
                if play_b.check_mouse_pos(mouse):
                    play_b = Button((180, 255, 100), (50, 550), (35, 100), "Sorting...")
                    play_b.draw(screen)
                    # Sorting algorithm goes here
                    done_b = Button((180, 255, 100), (50, 550), (35, 100), "Done!")
                    done_b.draw(screen)
                    pygame.display.update()
                elif back_b.check_mouse_pos(mouse):
                    main()

# ----------- End of Quick Sort function ----------- #


def heapify(heap, l, j, rec_list, screen, compare):
    """This function creates a Max Heap: Every root node is greater than its children
        parameters: heap, l = length of array, j = root node"""
    big = j
    left = 2 * j + 1
    right = 2 * j + 2
    if left < l and heap[left] > heap[j]:
        big = left

    if right < l and heap[right] > heap[big]:
        big = right

    # If the biggest element of the subtree is not the root of that
    # subtree, switch the nodes and then heapify again
    if big != j:
        # Swap the physical bars
        rec_list[j].swap(screen, rec_list[big])
        # Swap rectangle list bars
        r_temp = rec_list[j]
        rec_list[j] = rec_list[big]
        rec_list[big] = r_temp
        # Swap the array numbers
        temp = heap[j]
        heap[j] = heap[big]
        heap[big] = temp
        heapify(heap, l, big, rec_list, screen, compare)


def heap_sort(heap, screen, button_list, rectangle_list):
    """Imagine the array at a Binary Heap
       first, heapify to create a max heap
       next, swap the first and last elements in the heap
       last, heapify again"""
    play_b = button_list[0]
    back_b = button_list[1]
    comparisons = 0
    while True:
        pygame.display.update()
        for user_input in pygame.event.get():
            if user_input.type == QUIT:
                pygame.quit()
                quit()

            mouse = pygame.mouse.get_pos()
            if user_input.type == MOUSEBUTTONDOWN:
                if back_b.check_mouse_pos(mouse):
                    main()
                elif play_b.check_mouse_pos(mouse):
                    play_b = Button((180, 255, 100), (50, 550), (35, 100), "Sorting...")
                    play_b.draw(screen)
                    length = len(heap)
                    for j in range(length, -1, -1):
                        heapify(heap, length, j, rectangle_list, screen, comparisons)

                    for i in range(length-1, 0, -1):
                        # Swap the physical bars
                        rectangle_list[i].swap(screen, rectangle_list[0])
                        # Swap the rectangle list numbers
                        rec_temp = rectangle_list[i]
                        rectangle_list[i] = rectangle_list[0]
                        rectangle_list[0] = rec_temp
                        # Swap the array numbers
                        temp = heap[i]
                        heap[i] = heap[0]
                        heap[0] = temp
                        heapify(heap, i, 0, rectangle_list, screen, comparisons)
                    done_b = Button((180, 255, 100), (50, 550), (35, 100), "Done!")
                    done_b.draw(screen)
                    pygame.display.update()

# ----------- End of Heap Sort functions ----------- #
# ----------- Main is below ----------- #


def main():
    """array = [184, 131, 71, 57, 164, 112, 55, 69, 43, 182, 115, 16, 166, 142, 171, 144, 147,
             102, 50, 122, 38, 114, 19, 28, 173, 180, 113, 9, 10, 48, 70, 95, 13, 152, 17,
             110, 153, 170, 96, 128, 98, 157, 32, 25, 97, 7, 148, 72, 149, 172, 200, 175, 68,
             77, 36, 169, 54, 120, 185, 177, 163, 34, 61, 178, 193, 136, 42, 156, 130, 165,
             104, 119, 22, 100, 91, 37, 196, 92, 14, 3, 63, 168, 189, 62, 85, 183, 1, 90, 105,
             94, 158, 82, 159, 121, 132, 154, 133, 35, 127, 12, 137, 118, 129, 103, 79, 29,
             67, 51, 87, 5, 162, 181, 59, 6, 135, 101, 139, 58, 44, 160, 192, 75, 188, 64,
             195, 167, 123, 83, 52, 33, 81, 76, 155, 199, 106, 46, 65, 66, 141, 20, 15, 4,
             146, 145, 176, 151, 56, 88, 31, 134, 89, 126, 143, 140, 78, 190, 27, 116, 41,
             179, 26, 99, 125, 53, 197, 187, 39, 161, 186, 84, 107, 23, 150, 111, 109, 124, 8,
             174, 80, 198, 108, 18, 11, 117, 74, 138, 24, 86, 191, 73, 47, 45, 40, 2, 60, 49,
             93, 30, 194, 21]"""

    array = [46, 52, 5, 33, 28, 71, 37, 79, 23, 61, 10, 29, 39, 64, 60, 76, 86, 75, 87, 70,
             69, 8, 53, 25, 65, 42, 93, 30, 15, 59, 54, 7, 91, 82, 51, 18, 35, 88, 58, 6, 21,
             97, 34, 13, 62, 36, 99, 80, 68, 49, 11, 24, 92, 48, 26, 72, 89, 84, 22, 74, 100,
             14, 12, 96, 55, 77, 16, 19, 27, 66, 78, 85, 98, 83, 20, 57, 94, 41, 63, 43, 56,
             81, 31, 9, 95, 90, 40, 45, 32, 50, 3, 2, 4, 1, 67, 44, 38, 73, 17, 47]

    # Create UI
    pygame.init()
    display = pygame.display.set_mode((700, 600))  # x, y
    display.fill((215, 245, 255)) # Coffee Brown (200, 190, 140) //Moonlight (235, 245, 255)
    pygame.display.set_caption("Sorting Algorithms")
    t_font = pygame.font.SysFont("bahnschrift", 40, bold=True)
    title1 = t_font.render("Sorting Algorithm", False, (0, 0, 0))
    title2 = t_font.render("Visualizer!", False, (0, 0, 0))
    display.blit(title1, (165, 40))
    display.blit(title2, (230, 90))

    # Create all the buttons
    bubble_button = Button((180, 255, 100), (450, 175), (60, 150), "Bubble Sort")
    bubble_button.draw(display, (0, 0, 0))
    selection_button = Button((180, 255, 100), (450, 375), (60, 150), "Selection Sort")
    selection_button.draw(display, (0, 0, 0))
    heap_button = Button((180, 255, 100), (100, 175), (60, 150), "Heap Sort")
    heap_button.draw(display, (0, 0, 0))
    merge_button = Button((180, 255, 100), (100, 375), (60, 150), "Merge Sort")
    merge_button.draw(display, (0, 0, 0))
    quick_button = Button((180, 255, 100), (275, 275), (60, 150), "Quick Sort")
    quick_button.draw(display, (0, 0, 0))

    click = True  # This variable keeps track of if the mouse has been clicked
    clock = pygame.time.Clock()
    clock.tick(60)

    # Main display loop
    while True:
        pygame.display.update()
        for user_input in pygame.event.get():
            if user_input.type == QUIT:
                pygame.quit()
                quit()

            # ----- If the User hovers the mouse over a button ----- #
            m_pos = pygame.mouse.get_pos()
            if user_input.type == MOUSEMOTION and click:
                if bubble_button.check_mouse_pos(m_pos):
                    bubble_button.color = (255, 100, 100)
                    bubble_button.draw(display)
                else:
                    bubble_button.color = (180, 255, 100)
                    bubble_button.draw(display)

                if merge_button.check_mouse_pos(m_pos):
                    merge_button.color = (255, 100, 100)
                    merge_button.draw(display)
                else:
                    merge_button.color = (180, 255, 100)
                    merge_button.draw(display)

                if selection_button.check_mouse_pos(m_pos):
                    selection_button.color = (255, 100, 100)
                    selection_button.draw(display)
                else:
                    selection_button.color = (180, 255, 100)
                    selection_button.draw(display)

                if quick_button.check_mouse_pos(m_pos):
                    quick_button.color = (255, 100, 100)
                    quick_button.draw(display)
                else:
                    quick_button.color = (180, 255, 100)
                    quick_button.draw(display)

                if heap_button.check_mouse_pos(m_pos):
                    heap_button.color = (255, 100, 100)
                    heap_button.draw(display)
                else:
                    heap_button.color = (180, 255, 100)
                    heap_button.draw(display)

            # ----- If the user clicks on a button ----- #
            if user_input.type == MOUSEBUTTONDOWN:
                click = False
                if bubble_button.check_mouse_pos(m_pos):
                    new_display, b_list, br_list = sorting_screen(display, array)
                    bubble_sort(array, display, b_list, br_list)

                if merge_button.check_mouse_pos(m_pos):
                    new_display, b_list, br_list = sorting_screen(display, array)
                    merge_sort(array, display, b_list, br_list)

                if selection_button.check_mouse_pos(m_pos):
                    new_display, b_list, br_list = sorting_screen(display, array)
                    selection_sort(array, display, b_list, br_list)

                if quick_button.check_mouse_pos(m_pos):
                    new_display, b_list, br_list = sorting_screen(display, array)
                    quick_sort(array, display, b_list, br_list)

                if heap_button.check_mouse_pos(m_pos):
                    new_display, b_list, br_list = sorting_screen(display, array)
                    heap_sort(array, display, b_list, br_list)


main()

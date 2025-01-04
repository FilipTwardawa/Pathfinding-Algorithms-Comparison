"""
Chart Utilities Module

This module provides helper functions for creating bar charts and setting chart labels.
"""

import matplotlib.pyplot as plt


def plot_bar_chart(data, title, ylabel):
    """
    Helper function to plot bar charts.

    Args:
        data (dict): Data to plot.
        title (str): Chart title.
        ylabel (str): Label for the y-axis.
    """
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data.keys(), data.values(), color=["blue", "green", "orange"])

    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel("Algorithms", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    for bar_segment in bars:
        plt.text(
            bar_segment.get_x() + bar_segment.get_width() / 2,
            bar_segment.get_height(),
            f"{bar_segment.get_height():.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )
    plt.show()


def set_chart_labels(title, ylabel):
    """
    Helper function to set labels and grid on a chart.

    Args:
        title (str): Title of the chart.
        ylabel (str): Label for the y-axis.
    """
    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel("Algorithms", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)


def add_chart_labels(bars, format_str=":.2f"):
    """
    Helper function to add text labels on bars.

    Args:
        bars (list): List of bar segments.
        format_str (str): Format string for the labels.
    """
    for bar_segment in bars:
        plt.text(
            bar_segment.get_x() + bar_segment.get_width() / 2,
            bar_segment.get_height(),
            f"{bar_segment.get_height():{format_str}}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )



def generate_bar_chart(data, title, ylabel):
    """
    Helper function to generate bar charts.

    Args:
        data (dict): Dictionary containing the data to plot. Expected format is a dictionary
                     where keys are algorithm names and values are another dictionary with
                     keys such as 'cost' or 'time'.
        title (str): Title of the chart.
        ylabel (str): Label for the y-axis.
    """
    algorithms = list(data.keys())
    values = [metric['cost'] for metric in data.values()]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, values, color=["blue", "green", "orange"])

    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel("Algorithms", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    for bar_segment in bars:
        value = bar_segment.get_height()
        label_format = f"{value:.2f}" if isinstance(value, float) else f"{value}"
        plt.text(
            bar_segment.get_x() + bar_segment.get_width() / 2,
            value,
            label_format,
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.show()
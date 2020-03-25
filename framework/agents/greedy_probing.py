import tensorflow as tf
import numpy as np
from functools import partial
import typing

from problems import Problem
from .agent import GradientFreeAgent


class GreedyProbing(GradientFreeAgent):

    def choose_best_weight_update(self, weight_samples: tf.Tensor, weight_history: tf.Tensor, output_history: tf.Tensor, X: tf.Tensor, y: tf.Tensor) -> tf.Tensor:
        output_samples = self.predict_for_multiple_weights(weight_samples, X)
        distances_to_goal = tf.norm(output_samples - y, axis=-1)
        best = tf.argmin(distances_to_goal)
        return weight_samples[best]

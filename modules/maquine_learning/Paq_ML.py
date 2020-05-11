## INCLUYE TODOS LOS PAQUETES A USAR
# FUNCIONES DEFINIDAS PARA USO NECESARIO
import timeit
import time
import tensorflow as tf
import random
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import mpld3
import statistics as stats  # usar media o desviacion estandar
from IPython.display import clear_output  # CLEAR EL OUT USING COMMAND
import h5py
import os
import sys


## FUNCION PARA LLEVAR LA INFO DE SEGUNDOS A TIEMPO EXTENDIDO (DIAS/HORAS/MINUTOS/SEGUNDOS)
def frantime(segundos):
    dias = np.fix(segundos / 86400);
    hor = np.fix((segundos - dias * 86400) / 3600);
    min = np.fix((segundos - dias * 86400 - hor * 3600) / 60);
    seg = np.fix((segundos - dias * 86400 - hor * 3600 - min * 60));
    salida = [dias, hor, min, seg]
    return salida


## DEFINICION DE LOS MODOS DE ELECCION DE CAPAS OCULTAS Y NUMEROS DE NEURONAS
def neuronas(config):  # v_input, v_output, n_capas = 2, exp = 1,  modo = 'poly' ):
    x = np.ones(config.n_capas + 2)
    if config.exp >= 1:  # modo == 'poly':
        for i in range(config.n_capas + 2):
            x[len(x) - i - 1] = round((config.v_input - config.v_output) *
                                      pow(i / (config.n_capas + 1), config.exp) + config.v_output)
    elif config.exp < 1:
        for i in range(config.n_capas + 2):
            x[len(x) - i - 1] = round((config.v_input - config.v_output) *
                                      pow(i / (config.n_capas + 1), -1 / config.exp) + config.v_output)
    config.matrix_neuronas = np.int64(x)
    return config


# ORGANIZACION DE LA ESTRUCTURA INTERNA DE ENTRENAMIENTO #
def estructura(INPUT_LINEAL, OUTPUT_LINEAL, config):
    config = neuronas(config)
    # proceso iteractivo dinamico
    for i in range(len(config.matrix_neuronas) - 1):

        weights = tf.Variable(
            tf.random.truncated_normal([config.matrix_neuronas[i], config.matrix_neuronas[i + 1]], stddev=0.1),
            name=f"weights-w{i}")
        biases = tf.Variable(tf.constant(0.1, shape=[config.matrix_neuronas[i + 1]]), name=f"biases_b{i}")

        if i == 0:  # CONDICION INICIAL
            layer = tf.add(tf.matmul(config.X, weights), biases, name=f"layer_l{i}")
        else:  # VALORES INTERNMEDIOS
            layer = tf.add(tf.matmul(layer, weights), biases, name=f"layer_l{i}")
    # PARAMETROS FINALES PARA CARACTERIZACION
    config.cross_entropy = tf.reduce_mean(
        tf.compat.v2.nn.softmax_cross_entropy_with_logits(labels=config.Y, logits=layer),
        name="Definition_of_cross_entropy")
    config.train_step = tf.compat.v1.train.AdamOptimizer(config.learning_rate).minimize(config.cross_entropy,
                                                                                        name="Definition_of_train_step")
    config.correct_pred = tf.equal(tf.argmax(layer, 1), tf.argmax(config.Y, 1),
                                   name="Definition_of_correct_pred")
    config.accuracy = tf.reduce_mean(tf.cast(config.correct_pred, tf.float32),
                                     name="Definition_of_accuracy")
    return config


# INICIO DE LA ITERACION
def inicio(INPUT_LINEAL, INPUT_LINEAL_TEST, OUTPUT_LINEAL, OUTPUT_LINEAL_TEST, config):
    init = tf.compat.v1.global_variables_initializer()
    config.cost_summary = tf.compat.v1.summary.scalar("Cost", config.cross_entropy)
    config.acc_summary = tf.compat.v1.summary.scalar("Accuracy", config.accuracy)
    config.all_summary = tf.compat.v1.summary.merge_all()  # '''
    # saver=tf.train.Saver() #SALVAR LA SECCION PARA PODERLA UTILIZAR LUEGO
    with tf.compat.v1.Session() as sess:  # tf.Session() as sess:
        # writer = tf.summary.FileWriter("Tensorboard", sess.graph)
        writer = tf.compat.v1.summary.FileWriter("Tensorboard", sess.graph)
        # print(sess)
        sess.run(init)
        # saver.save(sess, 'modelo')
        toc_general = 0
        for i in range(config.n_iterations):
            tic = time.process_time()  # timeit.default_timer()
            sess.run(config.train_step, feed_dict={config.X: INPUT_LINEAL, config.Y: OUTPUT_LINEAL})  # CORRIDA

            config.summary_results, config.loss, config.acc = sess.run(
                [config.all_summary, config.cross_entropy, config.accuracy],
                feed_dict={config.X: INPUT_LINEAL, config.Y: OUTPUT_LINEAL})
            writer.add_summary(config.summary_results, i)

            toc = time.process_time()  # timeit.default_timer() ;
            toc_general += toc - tic
            if (i + 1) % config.n_step_visual_process == 0:
                print("\n | Info del modelo :: Iteration inst : ", '%.f' % i,
                      "\t | Accuracy =", '%.3f' % config.acc,
                      "\t | Loss =", '%.3f' % config.loss,
                      "\t | Time =", '%.3f' % (toc - tic))
            if config.acc > config.acc_corte:
                break
        config.test_accuracy, config.test_loss = sess.run([config.accuracy, config.cross_entropy],
                                                          feed_dict={config.X: INPUT_LINEAL_TEST,
                                                                     config.Y: OUTPUT_LINEAL_TEST})
        config.time_ite_mean = toc_general / (i + 1)
        config.n_iterations_acc = i
        print("\n | Info del modelo :: Iteration Max : ", '%.f' % config.n_iterations_acc,
              "\t | Accuracy : ", '%.3f' % config.acc,
              "\t | Loss : ", '%.3f' % config.loss,
              "\t | Mean time : ", '%.3f' % config.time_ite_mean, "\t |")
        print("\n | Info de test :: Accuracy : ", '%.3f' % config.test_accuracy,
              "\t | Loss : ", '%.3f' % config.test_loss, "\t |")

    return config

package model;

import java.io.Serializable;

public abstract class Animal implements Serializable {

    protected String nome;

    public Animal(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public abstract String emitirSom();
}

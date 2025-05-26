package com.example.management.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Entity
@Data
@Table(name = "departments")
public class Department {
        @Id
        private Integer id;
        @Column(nullable = false,length = 100)
        private String name;
        @Column(length = 100)
        private String location;

}

section .data
    cmd     db '/bin/cat',0
    arg1    db 'cat',0
    arg2    db 'arquivo.dat',0
    arg3    db '>',0
    arg4    db '/dev/null',0
    null    dq 0
    msg     db 'Tempo decorrido: ',0
    fmt     db '%f segundos',10,0

section .bss
    start   resq 1
    end     resq 1

section .text
    global _start

_start:
    ; get start time
    mov rax, 228         ; syscall: clock_gettime
    mov rdi, 0           ; CLOCK_REALTIME
    mov rsi, start
    syscall

    mov rcx, 1000
.loop:
    cmp rcx, 0
    je .wait

    mov rax, 57          ; syscall: fork
    syscall
    test rax, rax
    jnz .parent

    ; child process
    mov rax, 59          ; syscall: execve
    lea rdi, [rel cmd]
    lea rsi, [rel arg1]
    mov [rsp-32], rsi
    lea rsi, [rel arg2]
    mov [rsp-24], rsi
    mov qword [rsp-16], 0
    lea rsi, [rsp-32]
    mov rdx, 0
    syscall

    mov rax, 60          ; syscall: exit
    xor rdi, rdi
    syscall

.parent:
    dec rcx
    jmp .loop

.wait:
    mov rcx, 1000
.wait_loop:
    cmp rcx, 0
    je .get_end
    mov rax, 61          ; syscall: wait4
    mov rdi, -1
    mov rsi, 0
    mov rdx, 0
    mov r10, 0
    syscall
    dec rcx
    jmp .wait_loop

.get_end:
    mov rax, 228         ; syscall: clock_gettime
    mov rdi, 0
    mov rsi, end
    syscall

    ; (Printing elapsed time is complex in pure assembly; recommend using C for this part)
    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall
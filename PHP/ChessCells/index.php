<?php

function cellsAreSameColor(string $cell_a, string $cell_b) : bool {
    $cell_a = mb_strtolower($cell_a);
    $cell_b = mb_strtolower($cell_b);
    
    $input_cells_format = "/^[a-h]{1}[1-8]{1}$/u";

    if (!preg_match(input_cells_format, $cell_a) or !preg_match(input_cells_format, $cell_b)) {
        throw new Exception("Недопустимый формат! Обе переменные должны состоять из двух символов, из которых 1-ый — латинская буква от A до H, а 2-ой — цифра от 1 до 8.");
    }

    if ($cell_a === $cell_b) {
        return true;
    }

    $letters = "abcdefgh";

    $columns_are_same_parity = strpos($letters, $cell_a[0]) % 2 === strpos($letters, $cell_b[0]) % 2;
    $rows_are_same_parity = $cell_a[1] % 2 === $cell_b[1] % 2;
    
    return ($columns_are_same_parity and $rows_are_same_parity) or (!$columns_are_same_parity and !$rows_are_same_parity);
}

?>
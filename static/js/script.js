if (document.getElementById('comment-form')) {
    // Comment Characters Counter
    MAX_COMMENT_CHARS = 250
    const comment_textarea = document.getElementById('comment-textarea')
    const char_counter_field = document.getElementById('char-counter')

    comment_textarea.addEventListener("keyup", (e) => {
        const comment_length = comment_textarea.value.length
        const chars_remaining = MAX_COMMENT_CHARS - comment_length

        if (comment_length <= MAX_COMMENT_CHARS) {
            let chars = chars_remaining > 1 ? "characters" : "character"
            char_counter_field.textContent = `${chars_remaining} ${chars} remaining`
        }
    })
}
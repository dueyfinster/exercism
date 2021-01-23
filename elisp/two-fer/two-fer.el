;;; two-fer.el --- Two-fer Exercise (exercism)

;;; Commentary:

;;; Code:

(defun two-fer (&optional name)
  "Output 'one for NAME, one for me.' where name is 'you' if no argument supplied."
      (format "One for %s, one for me." (or name (setq name "you")))
  )

(provide 'two-fer)
;;; two-fer.el ends here

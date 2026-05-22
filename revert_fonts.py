import re

file_path = r'c:\Users\Admin\Music\AJK-addmission-redesign\AJK-addmission-page\styles.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Simple string replacements to revert the 40px changes
replacements = [
    # hero admission form card h3
    ('    font-size: 40px;\n    font-weight: 700;\n    line-height: 1.15;\n    text-align: center;\n    margin-bottom: 14px;',
     '    font-size: 24px;\n    font-weight: 800;\n    line-height: 1.15;\n    text-align: center;\n    margin-bottom: 14px;'),

    # purposeful-learning-title font-weight
    ('.purposeful-learning-title {\n    position: relative;\n    font-size: 40px;\n    font-weight: 700;',
     '.purposeful-learning-title {\n    position: relative;\n    font-size: 40px;\n    font-weight: 800;'),

    # stats-grid-number font-weight
    ('.stats-grid-number {\n    font-size: clamp(32px, 3vw, 46px);\n    font-weight: 700;',
     '.stats-grid-number {\n    font-size: clamp(32px, 3vw, 46px);\n    font-weight: 800;'),

    # core-values-title base
    ('.core-values-title {\n    font-size: 40px;',
     '.core-values-title {\n    font-size: 48px;'),

    # why-us-title base
    ('.why-us-title {\n    font-size: 40px;',
     '.why-us-title {\n    font-size: 46px;'),

    # why-us-item-title base
    ('.why-us-item-title {\n    font-size: 40px;',
     '.why-us-item-title {\n    font-size: 26px;'),

    # hiring-partners-title base
    ('.hiring-partners-title {\n    font-size: 40px;',
     '.hiring-partners-title {\n    font-size: 48px;'),

    # career-development-title base
    ('.career-development-title {\n    font-size: 40px;\n    font-weight: 700;',
     '.career-development-title {\n    font-size: clamp(34px, 3.2vw, 48px);\n    font-weight: 800;'),

    # career-dev-item-title base
    ('.career-dev-item-title {\n    font-size: 40px;\n    font-weight: 700;',
     '.career-dev-item-title {\n    font-size: 19px;\n    font-weight: 800;'),

    # why-parents-title base
    ('.why-parents-title {\n    font-size: 40px;\n    font-weight: 700;',
     '.why-parents-title {\n    font-size: clamp(38px, 4.4vw, 56px);\n    font-weight: 800;'),

    # parent-card-title base
    ('.parent-card-title {\n    font-size: 40px;',
     '.parent-card-title {\n    font-size: 20px;'),

    # cta-banner-title base
    ('.cta-banner-title {\n    font-size: 40px;',
     '.cta-banner-title {\n    font-size: 42px;'),

    # faculty-strength-title base
    ('.faculty-strength-title {\n    font-size: 40px;',
     '.faculty-strength-title {\n    font-size: 42px;'),

    # faculty-card-title base
    ('.faculty-card-title {\n    font-size: 40px;',
     '.faculty-card-title {\n    font-size: 18px;'),

    # ap-title base
    ('.ap-title {\n    font-size: 40px;\n    font-weight: 700;',
     '.ap-title {\n    font-size: clamp(36px, 4vw, 48px);\n    font-weight: 800;'),

    # ap-step-number font-weight
    ('    font-size: 56px;\n    font-weight: 700;',
     '    font-size: 56px;\n    font-weight: 900;'),

    # ap-step-text h3
    ('.ap-step-text h3 {\n    font-size: 40px;',
     '.ap-step-text h3 {\n    font-size: 17px;'),

    # infrastructure-learning-title base
    ('.infrastructure-learning-title {\n    font-size: 40px;',
     '.infrastructure-learning-title {\n    font-size: 44px;'),

    # infrastructure-path-title base
    ('.infrastructure-path-title {\n    font-size: 40px;\n    font-weight: 700;',
     '.infrastructure-path-title {\n    font-size: clamp(34px, 3.6vw, 48px);\n    font-weight: 800;'),

    # step-title base
    ('.step-title {\n    font-size: 40px;',
     '.step-title {\n    font-size: 20px;'),

    # admissions-simple-title base
    ('.admissions-simple-title {\n    font-size: 40px;',
     '.admissions-simple-title {\n    font-size: 42px;'),

    # form-box h3 base
    ('.form-box h3 {\n    font-size: 40px;',
     '.form-box h3 {\n    font-size: 32px;'),
]

# Also revert responsive media query overrides using line-by-line targeted substitution
responsive_replacements = [
    # 1024px breakpoints
    ('    .education-cta-title {\n        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px) {\n    .education-cta-content {',
     '    .education-cta-title {\n        font-size: 38px;\n    }\n}\n\n@media (max-width: 768px) {\n    .education-cta-content {'),

    ('    .careers-main-title {\n        font-size: 40px;\n    }\n\n    .careers-outline-title {\n        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px)',
     '    .careers-main-title {\n        font-size: 48px;\n    }\n\n    .careers-outline-title {\n        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px)'),

    ('    .core-values-title {\n        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px) {\n    .core-values-section',
     '    .core-values-title {\n        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px) {\n    .core-values-section'),

    ('        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px) {\n    .why-us-section {',
     '        font-size: 24px;\n    }\n}\n\n@media (max-width: 768px) {\n    .why-us-section {'),

    ('    .faculty-strength-title {\n        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px) {\n    .faculty-strength-content',
     '    .faculty-strength-title {\n        font-size: 36px;\n    }\n}\n\n@media (max-width: 768px) {\n    .faculty-strength-content'),

    ('    .ap-title {\n        font-size: 40px;\n    }',
     '    .ap-title {\n        font-size: 32px;\n    }'),

    # 768px breakpoints
    ('    .intro-title {\n        font-size: 40px;\n    }\n\n    .intro-content {',
     '    .intro-title {\n        font-size: 32px;\n    }\n\n    .intro-content {'),

    ('    .education-cta-title {\n        font-size: 40px;\n    }\n\n    .education-cta-description',
     '    .education-cta-title {\n        font-size: 32px;\n    }\n\n    .education-cta-description'),

    ('    .careers-main-title {\n        font-size: 40px;\n    }\n\n    .careers-focus-content',
     '    .careers-main-title {\n        font-size: 40px;\n    }\n\n    .careers-focus-content'),

    ('    .careers-outline-title {\n        font-size: 40px;\n        -webkit-text-stroke: 1.2px',
     '    .careers-outline-title {\n        font-size: 40px;\n        -webkit-text-stroke: 1.2px'),

    ('    .purposeful-learning-title {\n        font-size: 40px;\n    }\n\n    .purposeful-learning-text',
     '    .purposeful-learning-title {\n        font-size: 34px;\n    }\n\n    .purposeful-learning-text'),

    ('    .core-values-title {\n        font-size: 40px;\n    }\n\n    .value-text',
     '    .core-values-title {\n        font-size: 36px;\n    }\n\n    .value-text'),

    ('    .why-us-title {\n        font-size: 40px;\n        margin-bottom: 34px;\n    }\n\n    .why-us-item-title {\n        font-size: 40px;\n    }\n\n    .why-us-item-description',
     '    .why-us-title {\n        font-size: 38px;\n        margin-bottom: 34px;\n    }\n\n    .why-us-item-title {\n        font-size: 22px;\n    }\n\n    .why-us-item-description'),

    ('    .hiring-partners-title {\n        font-size: 40px;\n    }\n\n    .hiring-partners-text {\n        font-size: 15px',
     '    .hiring-partners-title {\n        font-size: 34px;\n    }\n\n    .hiring-partners-text {\n        font-size: 15px'),

    ('    .career-development-title {\n        font-size: 40px;\n        margin-bottom: 28px;\n    }',
     '    .career-development-title {\n        font-size: 34px;\n        margin-bottom: 28px;\n    }'),

    ('    .why-parents-title {\n        font-size: 40px;\n        margin-bottom: 42px;\n    }',
     '    .why-parents-title {\n        font-size: 36px;\n        margin-bottom: 42px;\n    }'),

    ('    .cta-banner-title {\n        font-size: 40px;\n    }\n\n    .cta-banner-description {\n        font-size: 15px',
     '    .cta-banner-title {\n        font-size: 30px;\n    }\n\n    .cta-banner-description {\n        font-size: 15px'),

    ('    .faculty-strength-title {\n        font-size: 40px;\n    }\n\n    .faculty-strength-subtitle',
     '    .faculty-strength-title {\n        font-size: 32px;\n    }\n\n    .faculty-strength-subtitle'),

    ('    .infrastructure-learning-title {\n        font-size: 40px;\n    }\n\n    .infrastructure-learning-cards',
     '    .infrastructure-learning-title {\n        font-size: 32px;\n    }\n\n    .infrastructure-learning-cards'),

    ('    .infrastructure-path-title {\n        font-size: 40px;\n        margin-bottom: 14px;\n    }',
     '    .infrastructure-path-title {\n        font-size: 30px;\n        margin-bottom: 14px;\n    }'),

    ('    .form-box h3 {\n        font-size: 40px;\n        margin-bottom: 20px;\n    }',
     '    .form-box h3 {\n        font-size: 26px;\n        margin-bottom: 20px;\n    }'),

    # 480px breakpoints
    ('    .intro-title {\n        font-size: 40px;\n    }\n\n    .intro-stats',
     '    .intro-title {\n        font-size: 28px;\n    }\n\n    .intro-stats'),

    ('    .education-cta-title {\n        font-size: 40px;\n    }\n\n    .review-avatars-image',
     '    .education-cta-title {\n        font-size: 28px;\n    }\n\n    .review-avatars-image'),

    ('    .careers-main-title {\n        font-size: 40px;\n    }\n\n    .careers-outline-title {\n        font-size: 40px;\n        -webkit-text-stroke: 1px',
     '    .careers-main-title {\n        font-size: 32px;\n    }\n\n    .careers-outline-title {\n        font-size: 32px;\n        -webkit-text-stroke: 1px'),

    ('    .purposeful-learning-title {\n        font-size: 40px;\n    }\n\n    .purposeful-learning-right',
     '    .purposeful-learning-title {\n        font-size: 30px;\n    }\n\n    .purposeful-learning-right'),

    ('    .core-values-title {\n        font-size: 40px;\n    }\n}',
     '    .core-values-title {\n        font-size: 32px;\n    }\n}'),

    ('    .why-us-title {\n        font-size: 40px;\n        margin-bottom: 28px;\n    }\n\n    .why-us-item-title {\n        font-size: 40px;\n    }\n}',
     '    .why-us-title {\n        font-size: 32px;\n        margin-bottom: 28px;\n    }\n\n    .why-us-item-title {\n        font-size: 20px;\n    }\n}'),

    ('    .hiring-partners-title {\n        font-size: 40px;\n    }\n\n    .partner-logo',
     '    .hiring-partners-title {\n        font-size: 28px;\n    }\n\n    .partner-logo'),

    ('    .career-development-title {\n        font-size: 40px;\n        margin-bottom: 24px;\n    }',
     '    .career-development-title {\n        font-size: 30px;\n        margin-bottom: 24px;\n    }'),

    ('    .why-parents-title {\n        font-size: 40px;\n    }\n\n    .parent-card {',
     '    .why-parents-title {\n        font-size: 28px;\n    }\n\n    .parent-card {'),

    ('    .parent-card-title {\n        font-size: 40px;\n    }\n\n    .center-image',
     '    .parent-card-title {\n        font-size: 18px;\n    }\n\n    .center-image'),

    ('    .cta-banner-title {\n        font-size: 40px;\n    }\n\n    .cta-banner-button',
     '    .cta-banner-title {\n        font-size: 24px;\n    }\n\n    .cta-banner-button'),

    ('    .faculty-strength-title {\n        font-size: 40px;\n    }\n\n    .faculty-feature-item',
     '    .faculty-strength-title {\n        font-size: 28px;\n    }\n\n    .faculty-feature-item'),

    ('    .infrastructure-learning-title {\n        font-size: 40px;\n    }\n\n    .infrastructure-learning-label',
     '    .infrastructure-learning-title {\n        font-size: 28px;\n    }\n\n    .infrastructure-learning-label'),

    ('    .infrastructure-path-title {\n        font-size: 40px;\n    }\n\n    .infrastructure-path-shell',
     '    .infrastructure-path-title {\n        font-size: 26px;\n    }\n\n    .infrastructure-path-shell'),

    ('    .step-title {\n        font-size: 40px;\n    }\n}\n\n/* ========================================',
     '    .step-title {\n        font-size: 16px;\n    }\n}\n\n/* ========================================'),

    ('        font-size: 40px;\n    }\n\n    .admissions-simple-content',
     '        font-size: 26px;\n    }\n\n    .admissions-simple-content'),

    ('    .form-box h3 {\n        font-size: 40px;\n    }\n\n    .npf_wgts',
     '    .form-box h3 {\n        font-size: 22px;\n    }\n\n    .npf_wgts'),

    # step-title inside 1024px media
    ('    .step-title {\n        font-size: 40px;\n    }\n}\n\n@media (max-width: 768px) {\n    .infrastructure-path-title',
     '    .step-title {\n        font-size: 17px;\n    }\n}\n\n@media (max-width: 768px) {\n    .infrastructure-path-title'),

    # admissions-simple-title inside 768px
    ('    .admissions-simple-title {\n        margin-top: 20px;\n        font-size: 40px;\n    }',
     '    .admissions-simple-title {\n        margin-top: 20px;\n        font-size: 20px;\n    }'),

    # admissions-simple-title inside 1024px
    ('    .admissions-simple-title {\n        font-size: 40px;\n    }\n\n    .icon-1',
     '    .admissions-simple-title {\n        font-size: 36px;\n    }\n\n    .icon-1'),

    # infrastructure-learning-title inside 1024px
    ('    .infrastructure-learning-title {\n        font-size: 40px;\n    }\n\n    .infrastructure-learning-cards',
     '    .infrastructure-learning-title {\n        font-size: 38px;\n    }\n\n    .infrastructure-learning-cards'),
]

for old, new in replacements:
    css = css.replace(old, new, 1)

for old, new in responsive_replacements:
    css = css.replace(old, new, 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('Done! All font sizes reverted to original values.')

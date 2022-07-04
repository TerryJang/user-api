-- USER --
DROP SCHEMA IF EXISTS develop;
CREATE SCHEMA develop;

DROP TABLE IF EXISTS develop.user;

-- USER --
CREATE TABLE develop.user (
                            id BIGINT NOT NULL AUTO_INCREMENT COMMENT '아이디',
                            email VARCHAR (255) NOT NULL COMMENT '이메일',
                            password VARCHAR (255) NOT NULL COMMENT '비밀번호',
                            status INTEGER NOT NULL DEFAULT 100 COMMENT '유저상태',
                            name VARCHAR (255) NOT NULL COMMENT '이름',
                            nickname VARCHAR (255) NOT NULL COMMENT '닉네임',
                            phone VARCHAR (20) NOT NULL COMMENT '핸드폰번호',
                            created_at DATETIME NOT NULL DEFAULT NOW() COMMENT '생성일',
                            updated_at DATETIME NOT NULL DEFAULT NOW() COMMENT '변경일',
    -- PRIMARY KEY --
                            CONSTRAINT PK_USER_ID PRIMARY KEY(ID)
    -- FOREIGN KEY --
    -- UNIQUE --
    -- CHECK --
)
;

CREATE INDEX IDX_USER_EMAIL ON develop.user (email ASC);
CREATE INDEX IDX_USER_STATUS ON develop.user (status ASC);
CREATE INDEX IDX_USER_CREATED ON develop.user (created_at DESC);
CREATE INDEX IDX_USER_UPDATED ON develop.user (updated_at DESC);


DROP TABLE IF EXISTS develop.auth_phone;

-- AUTH PHONE --
CREATE TABLE develop.auth_phone (
                              id BIGINT NOT NULL AUTO_INCREMENT COMMENT '아이디',
                              phone VARCHAR (20) NOT NULL COMMENT '핸드폰번호',
                              code VARCHAR (10) NOT NULL COMMENT '인증코드',
                              is_confirm BOOLEAN NOT NULL DEFAULT FALSE COMMENT '인증여부',
                              created_at DATETIME NOT NULL DEFAULT NOW() COMMENT '생성일',
                              updated_at DATETIME NOT NULL DEFAULT NOW() COMMENT '변경일',
    -- PRIMARY KEY --
                              CONSTRAINT PK_AUTH_PHONE_ID PRIMARY KEY(ID)
    -- FOREIGN KEY --
    -- UNIQUE --
    -- CHECK --
)
;

CREATE INDEX IDX_AUTH_PHONE_PHONE ON develop.auth_phone (phone ASC);
CREATE INDEX IDX_AUTH_PHONE_CREATED ON develop.auth_phone (created_at DESC);
CREATE INDEX IDX_AUTH_PHONE_UPDATED ON develop.auth_phone (updated_at DESC);


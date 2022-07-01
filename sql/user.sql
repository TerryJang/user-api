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
                            created DATETIME NOT NULL DEFAULT NOW() COMMENT '생성일',
                            updated DATETIME NOT NULL DEFAULT NOW() COMMENT '변경일',
    -- PRIMARY KEY --
                            CONSTRAINT PK_USER_ID PRIMARY KEY(ID)
    -- FOREIGN KEY --
    -- UNIQUE --
    -- CHECK --
)
;

CREATE INDEX IDX_USER_STATUS ON develop.user (status ASC);
CREATE INDEX IDX_USER_CREATED ON develop.user (created DESC);
CREATE INDEX IDX_USER_UPDATED ON develop.user (updated DESC);
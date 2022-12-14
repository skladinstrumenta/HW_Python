PGDMP         -                z           hw2    14.5    14.5     
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24641    hw2    DATABASE     `   CREATE DATABASE hw2 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE hw2;
                postgres    false            ?            1259    24643    actors    TABLE     q   CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying(100),
    birthday_year date
);
    DROP TABLE public.actors;
       public         heap    postgres    false            ?            1259    24642    actors_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.actors_id_seq;
       public          postgres    false    212                       0    0    actors_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;
          public          postgres    false    211            ?            1259    24653 	   directors    TABLE     `   CREATE TABLE public.directors (
    id integer NOT NULL,
    director character varying(100)
);
    DROP TABLE public.directors;
       public         heap    postgres    false            ?            1259    24652    directors_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.directors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.directors_id_seq;
       public          postgres    false    216                       0    0    directors_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.directors_id_seq OWNED BY public.directors.id;
          public          postgres    false    215            ?            1259    24648    films    TABLE     {   CREATE TABLE public.films (
    id integer NOT NULL,
    title character varying(100),
    genre character varying(100)
);
    DROP TABLE public.films;
       public         heap    postgres    false            ?            1259    24647    films_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.films_id_seq;
       public          postgres    false    214                       0    0    films_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.films_id_seq OWNED BY public.films.id;
          public          postgres    false    213            ?            1259    24658    ratings    TABLE     R   CREATE TABLE public.ratings (
    id integer NOT NULL,
    rating numeric(4,2)
);
    DROP TABLE public.ratings;
       public         heap    postgres    false            ?            1259    24657    ratings_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.ratings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.ratings_id_seq;
       public          postgres    false    218                       0    0    ratings_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.ratings_id_seq OWNED BY public.ratings.id;
          public          postgres    false    217            q           2604    24646 	   actors id    DEFAULT     f   ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);
 8   ALTER TABLE public.actors ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    211    212            s           2604    24656    directors id    DEFAULT     l   ALTER TABLE ONLY public.directors ALTER COLUMN id SET DEFAULT nextval('public.directors_id_seq'::regclass);
 ;   ALTER TABLE public.directors ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            r           2604    24651    films id    DEFAULT     d   ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);
 7   ALTER TABLE public.films ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213    214            t           2604    24661 
   ratings id    DEFAULT     h   ALTER TABLE ONLY public.ratings ALTER COLUMN id SET DEFAULT nextval('public.ratings_id_seq'::regclass);
 9   ALTER TABLE public.ratings ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218                      0    24643    actors 
   TABLE DATA           9   COPY public.actors (id, name, birthday_year) FROM stdin;
    public          postgres    false    212   ?                 0    24653 	   directors 
   TABLE DATA           1   COPY public.directors (id, director) FROM stdin;
    public          postgres    false    216                    0    24648    films 
   TABLE DATA           1   COPY public.films (id, title, genre) FROM stdin;
    public          postgres    false    214                    0    24658    ratings 
   TABLE DATA           -   COPY public.ratings (id, rating) FROM stdin;
    public          postgres    false    218                     0    0    actors_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.actors_id_seq', 4, true);
          public          postgres    false    211                       0    0    directors_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.directors_id_seq', 4, true);
          public          postgres    false    215                       0    0    films_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.films_id_seq', 3, true);
          public          postgres    false    213                       0    0    ratings_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.ratings_id_seq', 4, true);
          public          postgres    false    217               m   x?3?t?(?,V(J,?4?4??50?52?2??J,??S.MI???,ə?X?Zpsz??d&?)8%f怤Ltu??L8???3<?J?RK?&Z???L????? ???         ^   x???	?0 ?s3E&?̠P??x???BM%????۫???+?B|Dš0?h?B?fFG??R?5ٽ@kF???;x?)'b??L%?;???[ Jn?         v   x??;
?0??Y:?NP???},-t??:J#?? ?%?}K????C_?e˔F*?Pϑ?#[??? O!v???1?gi????ر?t6?L8M?'??07???-N?(_5(????!??
('         '   x?3???35?2???37?2?,?L8????b???? W?     